// Tarot Data extracted from index.html
const MAJOR = [
      { id: 0, name: 'Le Mat (El Loco)', marseilleName: 'Le Mat', numeral: '', art: '🤡', arcana: 'Mayor', v: 0 },
      { id: 1, name: 'Le Bateleur (El Mago)', marseilleName: 'Le Bateleur', numeral: 'I', art: '🎩', arcana: 'Mayor', v: 1 },
      { id: 2, name: 'La Papesse (La Papisa)', marseilleName: 'La Papesse', numeral: 'II', art: '📖', arcana: 'Mayor', v: 2 },
      { id: 3, name: "L'Impératrice (La Emperatriz)", marseilleName: "L'Impératrice", numeral: 'III', art: '👑', arcana: 'Mayor', v: 3 },
      { id: 4, name: "L'Empereur (El Emperador)", marseilleName: "L'Empereur", numeral: 'IIII', art: '⚔️', arcana: 'Mayor', v: 4 },
      { id: 5, name: 'Le Pape (El Papa)', marseilleName: 'Le Pape', numeral: 'V', art: '✝️', arcana: 'Mayor', v: 5 },
      { id: 6, name: "L'Amoureux (Los Enamorados)", marseilleName: "L'Amoureux", numeral: 'VI', art: '💑', arcana: 'Mayor', v: 6 },
      { id: 7, name: 'Le Chariot (El Carro)', marseilleName: 'Le Chariot', numeral: 'VII', art: '🏆', arcana: 'Mayor', v: 7 },
      { id: 8, name: 'La Justice (La Justicia)', marseilleName: 'La Justice', numeral: 'VIII', art: '⚖️', arcana: 'Mayor', v: 8 },
      { id: 9, name: "L'Hermite (El Ermitaño)", marseilleName: "L'Hermite", numeral: 'VIIII', art: '🕯️', arcana: 'Mayor', v: 9 },
      { id: 10, name: 'La Roue de Fortune (La Rueda)', marseilleName: 'La Roue', numeral: 'X', art: '☸️', arcana: 'Mayor', v: 10 },
      { id: 11, name: 'La Force (La Fuerza)', marseilleName: 'La Force', numeral: 'XI', art: '🦁', arcana: 'Mayor', v: 11 },
      { id: 12, name: 'Le Pendu (El Colgado)', marseilleName: 'Le Pendu', numeral: 'XII', art: '🔄', arcana: 'Mayor', v: 12 },
      { id: 13, name: '(La Muerte)', marseilleName: '', numeral: 'XIII', art: '💀', arcana: 'Mayor', v: 13 },
      { id: 14, name: 'Tempérance (La Templanza)', marseilleName: 'Tempérance', numeral: 'XIIII', art: '🏺', arcana: 'Mayor', v: 14 },
      { id: 15, name: 'Le Diable (El Diablo)', marseilleName: 'Le Diable', numeral: 'XV', art: '😈', arcana: 'Mayor', v: 15 },
      { id: 16, name: 'La Maison Dieu (La Torre)', marseilleName: 'La Maison Dieu', numeral: 'XVI', art: '🗼', arcana: 'Mayor', v: 16 },
      { id: 17, name: "L'Étoile (La Estrella)", marseilleName: "L'Étoile", numeral: 'XVII', art: '⭐', arcana: 'Mayor', v: 17 },
      { id: 18, name: 'La Lune (La Luna)', marseilleName: 'La Lune', numeral: 'XVIII', art: '🌙', arcana: 'Mayor', v: 18 },
      { id: 19, name: 'Le Soleil (El Sol)', marseilleName: 'Le Soleil', numeral: 'XIX', art: '☀️', arcana: 'Mayor', v: 19 },
      { id: 20, name: 'Le Jugement (El Juicio)', marseilleName: 'Le Jugement', numeral: 'XX', art: '📯', arcana: 'Mayor', v: 20 },
      { id: 21, name: 'Le Monde (El Mundo)', marseilleName: 'Le Monde', numeral: 'XXI', art: '🌍', arcana: 'Mayor', v: 21 },
    ];

const majorMeanings = {
        0: {
          significado: "El Loco representa los nuevos comienzos, la aventura y la fe ciega. Te invita a dar un salto a lo desconocido con optimismo.",
          palabrasClave: "Espontaneidad, Inocencia, Viajes, Potencial, Caos fértil",
          consejo: "Atrévete a experimentar sin planificar todo. El universo sostiene a quienes confían.",
          advertencia: "Cuidado con la imprudencia pura y los riesgos innecesarios sin red de seguridad."
        },
        1: {
          significado: "El Mago simboliza la manifestación, la destreza y el poder personal. Tienes a tu disposición todas las herramientas para hacer realidad tus metas.",
          palabrasClave: "Acción, Concentración, Habilidad, Voluntad, Ingenio",
          consejo: "Reclama tu poder y actúa con conciencia. Transforma las ideas en realidad enfocando tu energía.",
          advertencia: "Evita la manipulación o el uso egoísta de tus capacidades. No dejes tus talentos sin usar."
        },
        2: {
          significado: "La Papisa encarna la intuición, el misterio y la sabiduría interior. Hay conocimientos ocultos que están a punto de revelarse.",
          palabrasClave: "Intuición, Secretos, Sabiduría interior, Misticismo",
          consejo: "Escucha tu voz interna y confía en tus instintos. Es un momento para observar en lugar de actuar precipitadamente.",
          advertencia: "La desconexión emocional o el aislamiento extremo pueden bloquear tu verdadero entendimiento."
        },
        3: {
          significado: "La Emperatriz representa la abundancia, la fertilidad y la expresión creativa. Simboliza un periodo de prosperidad y crecimiento desbordante.",
          palabrasClave: "Creatividad, Fertilidad, Belleza, Abundancia, Naturaleza",
          consejo: "Nutre tus proyectos y relaciones. Disfruta de los placeres sensoriales y deja que tu lado creativo florezca.",
          advertencia: "Cuidado con el apego sofocante, la sobreprotección o el abandono de tu propio cuidado personal."
        },
        4: {
          significado: "El Emperador es el arquetipo de la estructura, la estabilidad y la autoridad. Habla de liderazgo y construcción sobre bases sólidas.",
          palabrasClave: "Estructura, Reglas, Disciplina, Liderazgo, Lógica",
          consejo: "Establece orden y toma el control de tu vida. La disciplina y la organización serán tus mejores aliados ahora.",
          advertencia: "Evita la tiranía, la rigidez mental extrema y el deseo desmedido de controlar a los demás."
        },
        5: {
          significado: "El Papa habla de tradición, creencias compartidas y enseñanza espiritual. Es la conexión entre lo terrenal y lo divino.",
          palabrasClave: "Tradición, Mentoría, Creencias, Valores compartidos",
          consejo: "Busca conocimiento en mentores o sistemas de valores establecidos. Aprende de la experiencia de otros.",
          advertencia: "Cuestiona el dogmatismo ciego o el seguir reglas anticuadas que ya no resuenan con tu verdad."
        },
        6: {
          significado: "Los Enamorados significan amor, armonía y elecciones trascendentales. Representa la alineación de tus valores personales.",
          palabrasClave: "Amor, Decisiones, Armonía, Unión, Valores",
          consejo: "Toma decisiones basadas en tu verdad interior y en el amor puro. Busca el equilibrio en tus relaciones.",
          advertencia: "La indecisión paralizante o elegir caminos fáciles pero deshonestos traerá desarmonía."
        },
        7: {
          significado: "El Carro simboliza la victoria, el control y la superación de obstáculos. El triunfo llega a través de tu esfuerzo dirigido.",
          palabrasClave: "Victoria, Determinación, Avance, Fuerza de voluntad",
          consejo: "Mantén la confianza para dirigir fuerzas opuestas hacia una sola dirección. Sigue adelante sin dudar.",
          advertencia: "No pases por encima de los demás para lograr tus metas. Controla tu agresividad."
        },
        8: {
          significado: "La Justicia encarna la equidad, la verdad y la ley kármica. Toda acción tiene una reacción; cosechas lo que siembras.",
          palabrasClave: "Equidad, Verdad, Karma, Responsabilidad, Equilibrio",
          consejo: "Actúa con integridad absoluta y busca el equilibrio en todas las áreas. Asume la responsabilidad de tus actos.",
          advertencia: "El autoengaño y la negación de la verdad atraerán consecuencias negativas severas."
        },
        9: {
          significado: "El Ermitaño es el buscador de la verdad. Representa la introspección, la soledad voluntaria y la guía interior.",
          palabrasClave: "Introspección, Soledad sabia, Búsqueda, Reflexión",
          consejo: "Haz una pausa para encontrar respuestas dentro de ti. Desconéctate del ruido exterior para escuchar tu alma.",
          advertencia: "El aislamiento prolongado puede convertirse en paranoia o miedo a conectar con los demás."
        },
        10: {
          significado: "La Rueda de la Fortuna indica ciclos, destino y puntos de inflexión. Habla de suerte inesperada y la intervención del karma.",
          palabrasClave: "Ciclos, Destino, Cambio inevitable, Suerte, Evolución",
          consejo: "Fluye con los cambios inevitables. Recuerda que lo que hoy está abajo, mañana estará arriba.",
          advertencia: "Aferrarse al pasado o resistirse al flujo natural de la vida solo traerá sufrimiento innecesario."
        },
        11: {
          significado: "La Fuerza no es violencia, sino el coraje, la persuasión y el dominio interior frente a instintos bajos.",
          palabrasClave: "Coraje, Resiliencia, Compasión, Paciencia, Dominio",
          consejo: "Enfrenta tus miedos y pasiones con compasión y resiliencia. Eres más fuerte de lo que crees.",
          advertencia: "No dejes que tus instintos primitivos, la ira o la inseguridad tomen el control de tus decisiones."
        },
        12: {
          significado: "El Colgado representa una pausa necesaria, la rendición y el sacrificio para obtener iluminación y otra perspectiva.",
          palabrasClave: "Pausa, Nuevas perspectivas, Rendición, Sacrificio",
          consejo: "Suspende tus acciones por ahora. Dejar ir la necesidad de control te traerá la respuesta que buscas.",
          advertencia: "Cuidado con el martirio inútil o estancarte en una posición de víctima sin propósito."
        },
        13: {
          significado: "La Muerte simboliza los finales inevitables, la transformación profunda y el cierre de un ciclo para un nuevo inicio.",
          palabrasClave: "Transformación, Finales, Renacimiento, Transición",
          consejo: "No temas al cambio. Cierra ese capítulo de forma definitiva para que lo nuevo pueda entrar a tu vida.",
          advertencia: "Aferrarse desesperadamente a lo que ya está muerto solo pudre el presente e impide tu evolución."
        },
        14: {
          significado: "La Templanza es el arte del equilibrio, la moderación y la sanación al mezclar elementos opuestos.",
          palabrasClave: "Equilibrio, Moderación, Sanación, Alquimia, Fluidez",
          consejo: "Busca el punto medio. Ten paciencia y mezcla los contrastes de tu vida para encontrar armonía.",
          advertencia: "Los extremos y los excesos te desestabilizarán. No te precipites en buscar resultados inmediatos."
        },
        15: {
          significado: "El Diablo refleja nuestras sombras, apegos materiales, tentaciones y adicciones que nos quitan la libertad.",
          palabrasClave: "Apegos, Sombra, Materialismo, Tentación, Ataduras",
          consejo: "Reconoce tus miedos ocultos y ataduras. La libertad empieza al iluminar tu propia oscuridad.",
          advertencia: "Estás atrapado en un ciclo tóxico o adicción. Es urgente cortar los lazos que te destruyen."
        },
        16: {
          significado: "La Torre marca un cambio repentino, una revelación disruptiva y el derrumbe de estructuras inestables.",
          palabrasClave: "Caos purificador, Revelación, Cambio drástico, Crisis",
          consejo: "Deja que caigan las ilusiones y cimientos falsos. De estas ruinas construirás una verdad más sólida.",
          advertencia: "Luchar contra esta caída solo hará que el impacto sea más doloroso. Acepta el desastre necesario."
        },
        17: {
          significado: "La Estrella trae esperanza, inspiración, sanación y renovación espiritual después de un periodo turbulento.",
          palabrasClave: "Esperanza, Renovación, Serenidad, Inspiración divina",
          consejo: "Confía plenamente, estás en el camino correcto y bendecido. Mantén la fe y sigue tu estrella guía.",
          advertencia: "Cuidado con perder la fe y caer en el cinismo o la desesperanza cuando la luz ya está brillando."
        },
        18: {
          significado: "La Luna representa la intuición profunda pero también la ilusión, los miedos irracionales y la confusión.",
          palabrasClave: "Ilusión, Miedos, Subconsciente, Intuición, Misterio",
          consejo: "Navega a través de tus miedos y confía en tu instinto. No todo es lo que parece en la superficie.",
          advertencia: "El autoengaño, la ansiedad proyectada y las paranoias te están nublando el juicio. Busca claridad."
        },
        19: {
          significado: "El Sol es la carta de la positividad radiante, el éxito, la vitalidad y la alegría absoluta.",
          palabrasClave: "Alegría, Éxito, Vitalidad, Claridad, Optimismo",
          consejo: "Disfruta de la calidez, confía en tu luz interior y celebra tus logros. Todo se está iluminando.",
          advertencia: "No dejes que tu ego se infle excesivamente ni te ciegues por un optimismo ingenuo."
        },
        20: {
          significado: "El Juicio es un despertar, una absolución y un llamado interior a renacer a un nivel de conciencia superior.",
          palabrasClave: "Renacimiento, Llamado, Absolución, Evaluación",
          consejo: "Evalúa tu vida con honestidad, perdona tu pasado y responde al llamado para evolucionar.",
          advertencia: "Ignorar este llamado o juzgarte a ti mismo con extrema dureza te dejará atascado en el pasado."
        },
        21: {
          significado: "El Mundo significa la completitud, la integración y la realización final de un largo viaje.",
          palabrasClave: "Plenitud, Realización, Integración, Éxito final",
          consejo: "Celebra la culminación de tu esfuerzo. Estás entero y listo para iniciar un ciclo aún mayor.",
          advertencia: "El estancamiento por falta de cierre o el temor a terminar una etapa te impiden alcanzar la plenitud."
        }
      };

const majorMeaningsRev = {
        0: {
          significado: "El Loco invertido indica actos temerarios, caos sin propósito o parálisis por miedo a lo desconocido.",
          palabrasClave: "Imprudencia, Temeridad, Irresponsabilidad, Miedo",
          consejo: "Mira antes de saltar. Evalúa los riesgos reales antes de tomar decisiones impulsivas y destructivas.",
          advertencia: "La negligencia y la falta de consideración por las consecuencias traerán problemas serios."
        },
        1: {
          significado: "El Mago invertido señala manipulación, ilusiones engañosas, potencial desperdiciado o falta de enfoque claro.",
          palabrasClave: "Manipulación, Engaño, Talento oculto, Dispersión",
          consejo: "Enfócate en intenciones honestas. Deja de desperdiciar tu energía en trucos y asume tu poder real.",
          advertencia: "Estás siendo engañado o te estás engañando a ti mismo utilizando tus talentos de forma destructiva."
        },
        2: {
          significado: "La Papisa invertida revela desconexión de la intuición, secretos oscuros o miedo a escuchar la voz interior.",
          palabrasClave: "Desconexión, Secretos negativos, Intuición bloqueada",
          consejo: "Reconecta contigo mismo en silencio. No ignores las señales sutiles que tu cuerpo y mente te dan.",
          advertencia: "La represión de la verdad o chismes malintencionados saldrán a la luz causando daño."
        },
        3: {
          significado: "La Emperatriz invertida muestra bloqueos creativos, asfixia emocional o descuido de las necesidades propias.",
          palabrasClave: "Bloqueo, Dependencia, Vacío, Asfixia",
          consejo: "Vuelve a conectar con la naturaleza y nutre tu propia alma antes de intentar cuidar a otros.",
          advertencia: "El exceso de control maternal o la negligencia hacia ti mismo agotarán tu fuerza vital."
        },
        4: {
          significado: "El Emperador invertido es el exceso de rigidez, el abuso de autoridad o, por el contrario, un caos inmaduro.",
          palabrasClave: "Tiranía, Caos, Rigidez, Inmadurez, Control excesivo",
          consejo: "Cede un poco de control y sé más flexible. Aprende a liderar inspirando en lugar de imponiendo.",
          advertencia: "El despotismo y la tiranía alejarán a las personas que necesitas para mantener tu reino en pie."
        },
        5: {
          significado: "El Papa invertido sugiere dogmatismo, rebeldía ciega o seguir a gurús y estructuras que carecen de verdad.",
          palabrasClave: "Dogma, Falso profeta, Rebeldía, Conformismo",
          consejo: "Rompe con las tradiciones que ya no te sirven. Crea tu propia brújula moral e intelectual.",
          advertencia: "Cuidado con los malos consejos, instituciones corruptas o el conformismo ciego que anula tu espíritu."
        },
        6: {
          significado: "Los Enamorados invertidos reflejan desarmonía, elecciones equivocadas o relaciones basadas en valores incompatibles.",
          palabrasClave: "Desequilibrio, Mala elección, Conflicto, Desconexión",
          consejo: "Reevalúa si tus elecciones actuales están realmente alineadas con tus principios más profundos.",
          advertencia: "Las decisiones basadas en gratificación instantánea o presiones externas fracturarán tu paz."
        },
        7: {
          significado: "El Carro invertido indica pérdida de dirección, agresividad sin control o barreras que parecen insuperables.",
          palabrasClave: "Falta de control, Dispersión, Bloqueos, Agresividad",
          consejo: "Detente un momento para recalibrar tus objetivos antes de estrellarte. Recupera la compostura.",
          advertencia: "Forzar las cosas usando agresividad desmedida te llevará a perder absolutamente todo."
        },
        8: {
          significado: "La Justicia invertida es el karma negativo no resuelto, la injusticia, parcialidad o huir de la responsabilidad.",
          palabrasClave: "Injusticia, Deshonestidad, Karma pendiente, Parcialidad",
          consejo: "Acepta tus errores y asume las consecuencias. Solo la verdad te permitirá volver al equilibrio.",
          advertencia: "El universo siempre equilibra la balanza; escapar de tus responsabilidades ahora empeorará tu deuda."
        },
        9: {
          significado: "El Ermitaño invertido señala soledad patológica, aislamiento tóxico o negarse a madurar y reflexionar.",
          palabrasClave: "Aislamiento, Paranoia, Rechazo de ayuda, Terquedad",
          consejo: "Es hora de salir de la cueva. Integra el aprendizaje en el mundo real y reconecta con otros.",
          advertencia: "El miedo al exterior y el orgullo ciego te están convirtiendo en un recluso sin sabiduría."
        },
        10: {
          significado: "La Rueda invertida muestra resistencia extrema al cambio, mala suerte temporal y ciclos destructivos que se repiten.",
          palabrasClave: "Estancamiento, Mala suerte, Resistencia, Repetición",
          consejo: "Deja de resistirte al giro inminente. Aprende la lección para poder romper el ciclo repetitivo.",
          advertencia: "Creerte víctima perpetua del destino te mantendrá atrapado indefinidamente en la misma miseria."
        },
        11: {
          significado: "La Fuerza invertida es dudar de uno mismo, debilidad interior o dejar que la ira cruda domine tus acciones.",
          palabrasClave: "Inseguridad, Impulsividad animal, Debilidad, Duda",
          consejo: "Vuelve a confiar en tu resiliencia silenciosa. Controla tus emociones antes de que te controlen a ti.",
          advertencia: "Actuar desde el ego frágil o la agresión pura es una muestra de debilidad, no de verdadero poder."
        },
        12: {
          significado: "El Colgado invertido advierte sobre sacrificios inútiles, estancamiento improductivo o terquedad egoísta.",
          palabrasClave: "Martirio, Estancamiento, Terquedad, Frustración",
          consejo: "Deja de hacer esfuerzos inútiles por algo que no cambia. Toma acción o asume una nueva estrategia.",
          advertencia: "Hacerte la víctima para manipular a otros o para no actuar solo prolongará tu agonía y la de los demás."
        },
        13: {
          significado: "La Muerte invertida es la negación profunda, la resistencia al final y el mantenimiento doloroso del status quo.",
          palabrasClave: "Estancamiento, Resistencia, Agonía, Miedo al cambio",
          consejo: "Suelta de una vez lo que ya no tiene vida. Permitir la limpieza es la única cura real para tu dolor.",
          advertencia: "Aferrarse desesperadamente a cosas obsoletas es emocionalmente cancerígeno y frena tu futuro."
        },
        14: {
          significado: "La Templanza invertida revela desequilibrio caótico, impaciencia y choques constantes de fuerzas opuestas.",
          palabrasClave: "Desequilibrio, Excesos, Impaciencia, Conflicto",
          consejo: "Baja la intensidad. Aléjate de los extremos y busca urgentemente un respiro para reequilibrarte.",
          advertencia: "Actuar de manera compulsiva, excesiva o extremista en este momento romperá estructuras importantes."
        },
        15: {
          significado: "El Diablo invertido es la posibilidad de liberarse de ataduras oscuras, superar adicciones o revelar secretos tóxicos.",
          palabrasClave: "Liberación, Superación, Desapego, Revelación",
          consejo: "Aprovecha la claridad. Rompe las cadenas ahora que finalmente ves cómo te limitaban.",
          advertencia: "Estar a punto de liberarte puede desencadenar miedos profundos; no regreses a tu zona de confort tóxica."
        },
        16: {
          significado: "La Torre invertida implica aferrarse a ruinas dolorosas, evitar el desastre a toda costa o una advertencia inminente.",
          palabrasClave: "Ruinas prolongadas, Negación de crisis, Miedo al dolor",
          consejo: "El cambio doloroso es inevitable; construir parches sobre terreno inestable solo pospone lo inevitable.",
          advertencia: "Resistir la caída de la torre hará que sufras el estrés del derrumbe por mucho más tiempo del necesario."
        },
        17: {
          significado: "La Estrella invertida señala desesperanza aplastante, desconexión del propósito espiritual y falta de fe.",
          palabrasClave: "Desánimo, Falta de fe, Desconexión, Cinismo",
          consejo: "Encuentra pequeñas fuentes de luz a tu alrededor. El universo no te ha abandonado, tú cerraste los ojos.",
          advertencia: "Permitir que el cinismo tome el control apagará toda posibilidad de inspiración y recuperación mágica."
        },
        18: {
          significado: "La Luna invertida indica que la confusión empieza a disiparse y emergen verdades ocultas, o un engaño profundo se revela.",
          palabrasClave: "Claridad, Secretos revelados, Superación de miedos",
          consejo: "Enfrenta valientemente la verdad cruda que ahora ves. Usa tu intuición para caminar hacia la luz.",
          advertencia: "Las mentiras y las ilusiones ya no te protegerán. Preparate para lidiar con el impacto de la realidad cruda."
        },
        19: {
          significado: "El Sol invertido es una vitalidad menguante, alegría aplazada temporalmente, ego herido o falta de entusiasmo verdadero.",
          palabrasClave: "Tristeza temporal, Ego excesivo, Falta de brillo",
          consejo: "Conecta con la gratitud por las pequeñas cosas para volver a encender tu fuego interno. Sé humilde.",
          advertencia: "La necesidad constante de atención y la arrogancia quemarán a quienes intentan calentarse en tu fuego."
        },
        20: {
          significado: "El Juicio invertido son dudas existenciales, negarse a evolucionar, juicios severos o quedarse anclado en remordimientos.",
          palabrasClave: "Dudas, Severidad, Estancamiento kármico, Culpa",
          consejo: "Perdónate. Deja de juzgarte tan duramente por el pasado y permítete avanzar hacia tu transformación.",
          advertencia: "Vivir en la culpa constante y el autojuicio severo te negará permanentemente el renacimiento."
        },
        21: {
          significado: "El Mundo invertido es la frustración por no alcanzar la meta, ciclos incompletos y falta de resolución definitiva.",
          palabrasClave: "Estancamiento, Frustración, Ciclos abiertos, Vacío",
          consejo: "Afronta las tareas pendientes. No te distraigas con nuevos proyectos antes de completar el actual.",
          advertencia: "Evitar el final de una etapa te mantendrá flotando en un limbo, sin poder abrazar una verdadera vida."
        }
      };
