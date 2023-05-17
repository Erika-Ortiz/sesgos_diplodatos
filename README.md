# ¡Bienvenidos a la mentoría "Sesgos Cognitivos en Razonamientos Lógicos"! 

**Mentora**: Lic. Erika R. Ortiz
**email**: erikarortiz@gmail.com 


<br>
En este proyecto, nos adentraremos en un tema que ha despertado gran interés en diferentes disciplinas: la influencia del conocimiento previo y sus efectos en el razonamiento lógico. Focalizaremos en el denominado "sesgo de creencia", caracterizado como la tendencia sistemática a evaluar la validez lógica de un argumento en función de la credibilidad de su conclusión. Es decir, tenemos la inclinación aceptar aquellos argumentos con conclusiones creíbles y a rechazar aquellos con conclusiones increíbles, sin importar la forma lógica de los argumentos en sí. <br>
<br></br>

![image](https://github.com/Erika-Ortiz/sesgos_diplodatos/assets/103912003/d754096e-013f-46ef-8e21-a65f6b682ca6)
<br></br>
### **Pero, ¿qué significa que un argumento sea *lógicamente válido*?**

Que un argumento sea lógicamente válido quiere decir que su conclusión se sigue de manera lógicamente necesaria de sus premisas,esto es, que **si las premisas de ese argumento fuesen verdaderas sería imposible que su conclusión fuese falsa**.

Por ejemplo, en el siguiente argumento, la conclusión se sigue de manera lógicamente necesaria de las premisas:

> Todos los rosarinos son argentinos <br>
> Messi es rosarino <br>
> Por lo tanto, Messi es argentino <br>

Sin embargo, en el siguiente ejemplo, la conclusión **no** se sigue de manera lógicamente necesaria de las premisas:

> Todos los rosarinos son argentinos <br>
> Messi es argentino <br>
> Por lo tanto, Messi es rosarino<br>

Porque del hecho de afirmar que todos los rosarinos son argentinos y que Messi es
argentino no se sigue de manera lógicamente necesaria que Messi sea rosarino, porque
Messi podría ser, por ejemplo, cordobés[^1].

Notemos que aunque este último argumento es inválido, su conclusión es creíble. Así, si aceptamos el argumento basándonos **sólo** en la credibilidad de la conclusión, estaríamos entonces ante un ***sesgo de creencia***. 

[^1]: Más info sobre la noción de consecuencia lógica [aquí.](https://es.wikipedia.org/wiki/Consecuencia_l%C3%B3gica)

<br></br>
## Datos 

Trabajaremos con datos reales obtenidos de una investigación interdisciplinaria en psicología cognitiva y filosofía de la lógica. Estos datos fueron recopilados a través de experimentos que se centraron en la evaluación individual y grupal de 8 argumentos. La tarea de evaluación consistió en que cada participante respondiera si creía, para cada uno de los diferentes argumentos presentados, si se trataba de argumento lógicamente válido o inválido (previa explicación del concepto de validez lógica con la utilización de ejemplos). 

Hicimos dos estudios: el primero con dos condiciones para diferentes participantes (diseño *between-subjects*), mientras que el segundo tiene tres condiciones para los mismos participantes (diseño *within-subjects*): resolución individual pre, resolución grupal y resolución individual post. A partir de ello, nuestros datasets quedaron de la siguiente manera: 


En el **primer conjunto de datos** - `dataset1_raw.csv`- algunos participantes resolvieron la tarea por su cuenta, mientras que otros trabajaron en grupos de 3 a 5 personas. El primer conjunto cuenta con 1913 filas y 13 columnas, correspondiente a un total de 239 participantes.


El **segundo conjunto de datos**  - `dataset2_raw.csv`- es aún más interesante, ya que los participantes realizaron la tarea en tres modalidades diferentes: primero individualmente, luego en grupo y finalmente de nuevo individualmente. Aquí, nuestro *dataset* recupera las respuestas dadas por un total de 115 participantes, constando de 2033 filas y también 13 columnas.<br></br>

![image](https://github.com/Erika-Ortiz/sesgos_diplodatos/assets/103912003/6e5af968-34ab-43ca-b333-08ab1ae40d15)
<br></br>
Ambos conjuntos de datos incluyen información sobre la edad, género, validez del argumento, creencia en la conclusión, aceptación del argumento, corrección de los resultados, forma en que se resolvió la tarea, entre otra información, que detallamos a continuación.
<br></br>
### Columnas y diccionario de valores

| Columna | Descripción | 
| ----------- | ----------- |
| `num` | Número de fila (1 a 1912 en el primer dataset, 1913 a 3944 en el segundo ) |
| `Participante` | Número asignado a cada participante de la muestra |
| `Lugar_admin` | Lugar donde se tomo la muestra[^2] |
| `Modalidad` | Modalidad de resolución de las tareas (**Resolución Grupal**, **Resolución Individual**, **Resolución Pre**, etc. ) |
| `Edad` | Edad del participante |
| `Género` | Género del participante (**F**= Femenino, **M**= Masculino, **O**= Otro) |
| `Grupo` | Número que identifica al grupo, con valores sólo en el segundo dataset (estudio *within-subjects*)|
| `Validez` | Validez del argumento evaluado ( **V**= válido, **I** = inválido) |
| `Creencia` | Creencia de la conclusión (**C** = creíble, **I** = increíble) |
| `ValidezxCreencia` | Combinación de las dos columnas previas (**VC**= válido creíble,**VI**= válido increíble, **IC**= inválido creíble **II**= inválido increíble) |
| `Silogismo` | Número que identifica a cada argumento de la tarea (valores enteros de 1 a 8) |
| `Aceptación` | Aceptación del argumento (**1** = acepta, **0** = no acepta) |
| `Correctas` | Coincidencia entre la respuesta dada y la validez del silogismo (**1** = correcta, **0** = incorrecta)[^3]|
<br>

[^2]: Datos obtenidos a través de muestreo por conveniencia. 
[^3]: Si el argumento es válido (V) y el/la participante acepta (1), la respuesta será correcta (= 1) 

Estos datos nos permitirán explorar y descubrir las diferencias en la evaluación de los argumentos según la forma en que se resolvieron y otras variables. Analizaremos la incidencia de diferentes variables en la aparición o mitigación de estos sesgos. Exploraremos cómo diferentes modalidades de resolución, ya sea en grupos o de manera individual, pueden afectar la manifestación de estos sesgos cognitivos. 

¡Pero no nos detendremos ahí! Uno de los objetivos principales de esta mentoría es detectar y predecir la aparición de los sesgos de creencia en pruebas de razonamiento. Para lograrlo, aplicaremos algoritmos de aprendizaje supervisado en un problema de regresión que consiste en predecir el "índice de creencia". Este índice es una variable numérica continua que calcularemos a partir de diversas variables en nuestro conjunto de datos.

<br></br>
## Hitos de la Mentoría


**Entrega 23/06 - Práctico 1 de análisis y visualización.**  En este práctico, nos adentramos en nuestros conjuntos de datos para:

- Identificar los tipos de variables que contienen.
- Calcular tendencias, dispersión y distribución de los datos.
- Analizar las relaciones entre las variables, utilizando gráficos que nos ayuden a visualizarlas.
Prestaremos especial atención a:<br>
	• La relación entre creencia y validez.<br>
	• La relación entre respuestas correctas y modalidades de resolución.<br>
- Utilizaremos funciones de Seaborn, como `gridplot`, `pairplot`, y parámetros como `hue`, que nos permitirán realizar visualizaciones comparativas de manera efectiva.

**Entrega 17/07 - Práctico 2 de análisis exploratorio y curación de datos**, que consiste en profundizar en lo trabajado en el práctico anterior y preparar los datos para aplicar algoritmos de machine learning en el próximo práctico.
- Pondremos nuestros datos en un único dataset.
- Trabajaremos en la identificación de *outliers*, imputación de valores faltantes, conversión de datos categóricos, etc.
- Una actividad destacada será la creación de una columna llamada "índice de creencia", que será nuestra variable a predecir en el siguiente práctico ☺

**Entrega 27/07 - Video de presentación intermedia del proyecto y dataset**<br>

**Entrega 11/09 - Práctico 3 de aprendizaje supervisado**, que consistirá en aplicar algoritmos de regresión de aprendizaje supervisado para predecir los índices de creencias en razonamientos lógicos y detectar posibles sesgos.
- Comenzaremos utilizando un modelo base (*baseline model*) como referencia para comparar con otros modelos en la resolución de nuestro problema.
- Realizaremos optimización de hiperpárametros utilizando técnicas como grid search y random search.
- Seleccionaremos métricas de error como MAE, MSE y RMSE, para evaluar nuestros modelos <br>

**Entrega 23/09 - Video de presentación final de mentoría**<br>

**Jornadas 10/11 y 11/11 - Presentación de mentorías**<br>

