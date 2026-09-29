import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.ensemble import RandomForestRegressor
from collections import Counter
import random

class BalotoPredictor:
    def __init__(self, history):
        """
        history es una lista de diccionarios:
        [{'type': 'Baloto', 'main_balls': [1,2,3,4,5], 'super_ball': 6}, ...]
        """
        self.history = history
        
    def _get_time_series(self):
        """Prepara las series de tiempo para las 5 posiciones y la súper balota."""
        if not self.history:
            return None
            
        # Tomaremos todos los sorteos combinados o podríamos separarlos. 
        # Aquí combinamos todo para mayor volumen de datos matemáticos.
        series = {
            'pos_0': [], 'pos_1': [], 'pos_2': [], 'pos_3': [], 'pos_4': [], 'super': []
        }
        
        for draw in self.history:
            balls = sorted(draw['main_balls']) # Aseguramos orden para que las posiciones tengan sentido
            if len(balls) == 5:
                series['pos_0'].append(balls[0])
                series['pos_1'].append(balls[1])
                series['pos_2'].append(balls[2])
                series['pos_3'].append(balls[3])
                series['pos_4'].append(balls[4])
                series['super'].append(draw['super_ball'])
                
        return series

    def predict_linear(self):
        """Aplica Regresión Lineal para proyectar la siguiente balota de cada posición."""
        series = self._get_time_series()
        if not series or len(series['pos_0']) < 2:
            return self.fallback_prediction()
            
        prediction = []
        n = len(series['pos_0'])
        X = np.array(range(n)).reshape(-1, 1) # Tiempo (índice del sorteo)
        
        for i in range(5):
            y = np.array(series[f'pos_{i}'])
            model = LinearRegression().fit(X, y)
            # Predecir el paso n
            next_val = int(round(model.predict([[n]])[0]))
            next_val = max(1, min(43, next_val)) # Acotar al rango válido
            prediction.append(next_val)
            
        # Super balota
        y_super = np.array(series['super'])
        model_super = LinearRegression().fit(X, y_super)
        next_super = int(round(model_super.predict([[n]])[0]))
        next_super = max(1, min(16, next_super))
        
        # Validar duplicados en main balls (Regresión Lineal no sabe de unicidad)
        prediction = self._fix_duplicates(prediction, 43)
        return {"main_balls": sorted(prediction), "super_ball": next_super}

    def predict_polynomial(self, degree=3):
        """Aplica Regresión Polinómica para capturar oscilaciones."""
        series = self._get_time_series()
        # Si no hay datos suficientes para un polinomio de grado 3, bajamos a grado menor
        if not series or len(series['pos_0']) < degree + 1:
            return self.predict_linear()
            
        prediction = []
        n = len(series['pos_0'])
        X = np.array(range(n)).reshape(-1, 1)
        poly = PolynomialFeatures(degree=degree)
        X_poly = poly.fit_transform(X)
        X_next = poly.transform([[n]])
        
        for i in range(5):
            y = np.array(series[f'pos_{i}'])
            model = LinearRegression().fit(X_poly, y)
            next_val = int(round(model.predict(X_next)[0]))
            next_val = max(1, min(43, next_val))
            prediction.append(next_val)
            
        y_super = np.array(series['super'])
        model_super = LinearRegression().fit(X_poly, y_super)
        next_super = int(round(model_super.predict(X_next)[0]))
        next_super = max(1, min(16, next_super))
        
        prediction = self._fix_duplicates(prediction, 43)
        return {"main_balls": sorted(prediction), "super_ball": next_super}
        
    def predict_frequency(self):
        """Análisis probabilístico basado en las frecuencias de aparición (Ley de Grandes Números)."""
        series = self._get_time_series()
        if not series:
            return self.fallback_prediction()
            
        all_main_balls = []
        for i in range(5):
            all_main_balls.extend(series[f'pos_{i}'])
            
        counts = Counter(all_main_balls)
        # Tomamos los 5 más comunes
        most_common = [num for num, _ in counts.most_common(5)]
        
        # Si no hay 5, llenamos con aleatorios no repetidos
        most_common = self._fill_random_unique(most_common, 5, 43)
        
        super_counts = Counter(series['super'])
        most_common_super = super_counts.most_common(1)
        if most_common_super:
            next_super = most_common_super[0][0]
        else:
            next_super = random.randint(1, 16)
            
        return {"main_balls": sorted(most_common), "super_ball": next_super}

    def predict_markov(self):
        """Cadenas de Markov: Probabilidad de transición entre números."""
        series = self._get_time_series()
        if not series or len(series['pos_0']) < 2:
            return self.fallback_prediction()
            
        prediction = []
        for i in range(5):
            seq = series[f'pos_{i}']
            last_val = seq[-1]
            # Buscar transiciones desde last_val
            transitions = []
            for j in range(len(seq)-1):
                if seq[j] == last_val:
                    transitions.append(seq[j+1])
            
            if transitions:
                # El más probable que siga
                next_val = Counter(transitions).most_common(1)[0][0]
            else:
                # Si nunca se ha visto, elegir uno frecuente
                next_val = Counter(seq).most_common(1)[0][0]
            prediction.append(next_val)
            
        super_seq = series['super']
        last_super = super_seq[-1]
        super_trans = [super_seq[j+1] for j in range(len(super_seq)-1) if super_seq[j] == last_super]
        next_super = Counter(super_trans).most_common(1)[0][0] if super_trans else Counter(super_seq).most_common(1)[0][0]
        
        prediction = self._fix_duplicates(prediction, 43)
        return {"main_balls": sorted(prediction), "super_ball": next_super}

    def predict_random_forest(self):
        """Bosques Aleatorios (Machine Learning) para encontrar patrones complejos."""
        series = self._get_time_series()
        if not series or len(series['pos_0']) < 2:
            return self.fallback_prediction()
            
        prediction = []
        n = len(series['pos_0'])
        X = np.array(range(n)).reshape(-1, 1)
        
        for i in range(5):
            y = np.array(series[f'pos_{i}'])
            model = RandomForestRegressor(n_estimators=100, random_state=42).fit(X, y)
            next_val = int(round(model.predict([[n]])[0]))
            next_val = max(1, min(43, next_val))
            prediction.append(next_val)
            
        y_super = np.array(series['super'])
        model_super = RandomForestRegressor(n_estimators=100, random_state=42).fit(X, y_super)
        next_super = int(round(model_super.predict([[n]])[0]))
        next_super = max(1, min(16, next_super))
        
        prediction = self._fix_duplicates(prediction, 43)
        return {"main_balls": sorted(prediction), "super_ball": next_super}

    def predict_spatial_entropy(self):
        """Análisis Espacial Combinatorio: Busca equilibrio (ej. pares/impares)."""
        # Generamos combinaciones y filtramos la que tenga mejor "entropía"
        best_combo = []
        for _ in range(50):
            combo = sorted(random.sample(range(1, 44), 5))
            evens = sum(1 for x in combo if x % 2 == 0)
            odds = 5 - evens
            # Un equilibrio ideal es 2-3 o 3-2 en pares/impares
            if evens in [2, 3]:
                # Y que no estén todos pegados (verificando el rango máximo-mínimo)
                if combo[-1] - combo[0] > 20: 
                    best_combo = combo
                    break
        if not best_combo:
            best_combo = sorted(random.sample(range(1, 44), 5))
            
        super_ball = random.choice([x for x in range(1, 17) if x % 2 != 0]) # Ejemplo de sesgo espacial
        return {"main_balls": best_combo, "super_ball": super_ball}

    def predict_genetic_algorithm(self):
        """Biología: Algoritmo Genético (Evolución de Darwin)."""
        # Población inicial
        population = [sorted(random.sample(range(1, 44), 5)) for _ in range(50)]
        series = self._get_time_series()
        
        # Genes fuertes: los números más frecuentes históricamente
        if not series: return self.fallback_prediction()
        all_main = []
        for i in range(5): all_main.extend(series[f'pos_{i}'])
        counts = Counter(all_main)
        
        for generation in range(20):
            # Fitness: ¿cuántos genes fuertes tiene el individuo?
            fitness_scores = []
            for ind in population:
                score = sum(counts[gen] for gen in ind)
                fitness_scores.append((score, ind))
            
            # Selección natural: Sobreviven los mejores 25
            fitness_scores.sort(key=lambda x: x[0], reverse=True)
            survivors = [x[1] for x in fitness_scores[:25]]
            
            # Cruce y Mutación (reproducción)
            next_gen = list(survivors)
            while len(next_gen) < 50:
                parent = random.choice(survivors)
                child = list(parent)
                # Mutar un gen
                idx_mut = random.randint(0, 4)
                new_gene = random.randint(1, 43)
                if new_gene not in child:
                    child[idx_mut] = new_gene
                next_gen.append(sorted(child))
            population = next_gen
            
        best_main = fitness_scores[0][1]
        super_ball = random.randint(1, 16)
        return {"main_balls": sorted(best_main), "super_ball": super_ball}

    def predict_thermodynamics(self):
        """Física: Cinética de Gases y Distribución de Maxwell-Boltzmann."""
        series = self._get_time_series()
        if not series: return self.fallback_prediction()
        
        all_main = []
        for i in range(5): all_main.extend(series[f'pos_{i}'])
        counts = Counter(all_main)
        
        # Encontrar "tiempo desde última aparición" para cada balota (1 a 43)
        time_since_last = {k: 100 for k in range(1, 44)} # 100 sorteos por defecto (frío)
        num_draws = len(series['pos_0'])
        
        for i in range(5):
            seq = series[f'pos_{i}']
            for draw_idx, ball in enumerate(seq):
                # Distancia desde el final
                dist = num_draws - draw_idx
                if dist < time_since_last[ball]:
                    time_since_last[ball] = dist
                    
        # Calcular Energía Cinética (Ek = 1/2 * m * v^2)
        # masa (m) = inercia histórica (frecuencia)
        # velocidad (v) = 1 / tiempo_desde_ultima (balotas recientes rebotan más rápido)
        ek_scores = []
        for ball in range(1, 44):
            m = counts.get(ball, 1)
            v = 1.0 / (time_since_last[ball] + 1)
            ek = 0.5 * m * (v ** 2)
            ek_scores.append((ek, ball))
            
        # Las partículas que escapan tienen la mayor energía cinética
        ek_scores.sort(key=lambda x: x[0], reverse=True)
        top_kinetic = [x[1] for x in ek_scores[:5]]
        
        return {"main_balls": sorted(top_kinetic), "super_ball": random.randint(1, 16)}

    def predict_radioactive_decay(self):
        """Física Cuántica: Ley de Decaimiento Radiactivo de Poisson."""
        series = self._get_time_series()
        if not series: return self.fallback_prediction()
        
        time_since_last = {k: 100 for k in range(1, 44)}
        num_draws = len(series['pos_0'])
        
        for i in range(5):
            seq = series[f'pos_{i}']
            for draw_idx, ball in enumerate(seq):
                dist = num_draws - draw_idx
                if dist < time_since_last[ball]:
                    time_since_last[ball] = dist
                    
        # Los isótopos inestables son los que llevan mucho tiempo sin decaer (mayor vida media acumulada).
        # Tienen mayor probabilidad cuántica de colapsar hoy.
        # Ordenamos por mayor 'time_since_last'.
        decay_probs = []
        for ball in range(1, 44):
            # Simulamos constante lambda aleatoria por la naturaleza cuántica
            lambd = random.uniform(0.01, 0.1)
            t = time_since_last[ball]
            # Probabilidad de decaimiento = 1 - e^(-lambda * t)
            prob_decay = 1 - np.exp(-lambd * t)
            decay_probs.append((prob_decay, ball))
            
        decay_probs.sort(key=lambda x: x[0], reverse=True)
        unstable_isotopes = [x[1] for x in decay_probs[:5]]
        
        return {"main_balls": sorted(unstable_isotopes), "super_ball": random.randint(1, 16)}

    def predict_expert(self):
        """Unifica predicciones para sugerir un pronóstico experto balanceado."""
        lin = self.predict_linear()
        poly = self.predict_polynomial(degree=2)
        freq = self.predict_frequency()
        markov = self.predict_markov()
        rf = self.predict_random_forest()
        spatial = self.predict_spatial_entropy()
        genetic = self.predict_genetic_algorithm()
        thermo = self.predict_thermodynamics()
        radio = self.predict_radioactive_decay()
        
        expert_main = []
        pool = (lin['main_balls'] + poly['main_balls'] + freq['main_balls'] + 
                markov['main_balls'] + rf['main_balls'] + spatial['main_balls'] +
                genetic['main_balls'] + thermo['main_balls'] + radio['main_balls'])
        
        counts = Counter(pool)
        for num, count in counts.most_common(5):
            expert_main.append(num)
            
        expert_main = self._fill_random_unique(expert_main, 5, 43)
        
        super_pool = [lin['super_ball'], poly['super_ball'], freq['super_ball'], 
                      markov['super_ball'], rf['super_ball'], spatial['super_ball'],
                      genetic['super_ball'], thermo['super_ball'], radio['super_ball']]
        super_counts = Counter(super_pool)
        expert_super = super_counts.most_common(1)[0][0]
        
        return {"main_balls": sorted(expert_main), "super_ball": expert_super}
        
    def fallback_prediction(self):
        """Si no hay datos, retorna números aleatorios matemáticamente válidos."""
        main_balls = random.sample(range(1, 44), 5)
        super_ball = random.randint(1, 16)
        return {"main_balls": sorted(main_balls), "super_ball": super_ball}

    def _fix_duplicates(self, numbers, max_val):
        """Asegura que no haya números repetidos en un sorteo."""
        unique_nums = []
        for num in numbers:
            while num in unique_nums:
                num += 1
                if num > max_val:
                    num = 1
            unique_nums.append(num)
        return unique_nums
        
    def _fill_random_unique(self, current_list, target_length, max_val):
        """Completa una lista hasta target_length con valores únicos aleatorios."""
        result = list(current_list)
        while len(result) < target_length:
            rand_num = random.randint(1, max_val)
            if rand_num not in result:
                result.append(rand_num)
        return result
