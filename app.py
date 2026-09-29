from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime, timedelta
from baloto_scraper import BalotoScraper
from baloto_predictor import BalotoPredictor

app = Flask(__name__, template_folder=".", static_folder=".", static_url_path="")

def get_next_draw_date():
    d = datetime.now()
    # Si hoy es día de sorteo pero ya pasó la hora (ej. 23:00), calculamos el siguiente
    if d.weekday() in [0, 2, 5] and d.hour >= 23:
        d += timedelta(days=1)
        
    # En Python weekday(): 0=Lunes, 2=Miércoles, 5=Sábado
    while d.weekday() not in [0, 2, 5]:
        d += timedelta(days=1)
        
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    return f"{dias[d.weekday()]} {d.day} de {meses[d.month - 1]} de {d.year}"

@app.route('/')
def index():
    # Sirve el index.html original (que ha sido modificado para incluir el boton)
    return app.send_static_file('index.html')

@app.route('/taboo')
def taboo():
    return app.send_static_file('taboo.html')

@app.route('/history')
def history():
    scraper = BalotoScraper()
    # Actualizar resultados automáticamente al entrar al historial
    results = scraper.scrape_current_results()
    if results:
        scraper.save_history(results)
        
    history_data = scraper.load_history()
    # Invertir para que los sorteos más recientes salgan arriba
    history_data.reverse()
    return render_template('history.html', history=history_data)

@app.route('/predict')
def predict():
    # Ejecuta la logica del matemático
    scraper = BalotoScraper()
    results = scraper.scrape_current_results()
    if results:
        scraper.save_history(results)
    
    history = scraper.load_history()
    
    if not history:
        return "<h1>Error: No hay datos en el historial para predecir.</h1>", 500
        
    predictor = BalotoPredictor(history)
    lin_pred = predictor.predict_linear()
    poly_pred = predictor.predict_polynomial(degree=2)
    freq_pred = predictor.predict_frequency()
    markov_pred = predictor.predict_markov()
    rf_pred = predictor.predict_random_forest()
    spatial_pred = predictor.predict_spatial_entropy()
    genetic_pred = predictor.predict_genetic_algorithm()
    thermo_pred = predictor.predict_thermodynamics()
    radio_pred = predictor.predict_radioactive_decay()
    expert_pred = predictor.predict_expert()
    
    next_date = get_next_draw_date()
    
    return render_template('results.html', 
                           lin=lin_pred, 
                           poly=poly_pred, 
                           freq=freq_pred, 
                           markov=markov_pred,
                           rf=rf_pred,
                           spatial=spatial_pred,
                           genetic=genetic_pred,
                           thermo=thermo_pred,
                           radio=radio_pred,
                           expert=expert_pred,
                           next_date=next_date)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
