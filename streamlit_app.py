import os
import openai

openai.api_key = os.getenv("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")

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt="Corrija la ortografía y la puntuación del siguiente texto. Tome en cuenta que esto no es un diálogo, sino corrección de estilo; por consiguiente, si el texto que se le presenta es una pregunta, trátelo como texto que hay que revisar y corregir, no como pregunta que hay que responder. Agregue punto al final de las frases sin punto o de las palabras sueltas. Quite o agregue las comas que sean necesarias, o bien, cámbielas por punto o por punto y coma, según se requiera. Divida los párrafos largos en párrafos más cortos, cuidando de que cada uno desarrolle una idea. Comience los textos con letra inicial mayúscula, y tilde las mayúsculas que lo necesiten, como en «MAYÚSCULA». Cambie las comillas inglesas por españolas o angulares. Divida los párrafos largos en párrafos cortos, cuando así convenga. Consulte: https://www.fundeu.es.\nQ: El coraje también se entrena: palabra de Pau Gasol. no kiero bolver a verte le dijo la mujer a su marido este se fue sin responderle, nda. es que no me entiendes??? ya no quiero saber nadA de tí. Por el profesor moris polanco autor de 4 libros de filosofía La tarde esta marabillosa es encantador poder decir te quiero vida mia ya bamos superando los errores evidentes pero no quuiero sacarlo al publico toavia porque siepre va a ver errores. Coomo lograr que sea perfexcto??? Que canssancio hoy por dios santo y pensar que esto tiene aue salir rebien por cierto como se escribirá Solares de Villarreal o de Villareal??? Esto, no esta funsionando como drebeira de funcionari no es cierto Muy bien, veamos si es capaz de poner \"signos\" de EXCLAMACION o de interrogacion. \nA: «El coraje también se entrena»: palabras de Pau Gasol. «No quiero volver a verte», le dijo la mujer a su marido; este se fue sin responderle nada. «¿Es que no me entiendes?». Ya no quiero saber nada de ti. Por el profesor Moris Polanco, autor de cuatro libros de filosofía. La tarde está maravillosa; es encantador poder decir «te quiero, vida mía». Ya vamos superando los errores evidentes, pero no quiero hacerlo público aún porque tiene errores. ¿Cómo lograr que sea perfecto? ¡Qué cansancio hoy, por Dios santo! Y pensar que esto tiene que salir bien... Por cierto, ¿cómo se escribirá: «Solares de Villarreal» o «de Villareal»? Esto no está funcionando como debería, ¿no es cierto? Muy bien: veamos si es capaz de poner «signos» de EXCLAMACIÓN o de interrogación. \n###\nQ: pOR QUÉ NO LO HARIA? \"Este es un texto como comillas españolas\" ¿Estara consultando las dos obras que le dije? No parece, porque no cambia la abreviatura de Dª., o sí? Erase una mañana fria y gris, Caperucita le dijo a su mama voy a llevarle su comida a mi abue. Me dijo de  que no era cierto La convenció que viniera con nosotros La dijo que no quería comer chocolate “Sólo\" nunca lleva tilde según las nuevas normas. Beamos esto Necesito que me de dinero. Para asistir el día de mañana 24 de marzo a las 8:50 a.m. solo da click al siguiente botón. Creo que eventualmente cederá. Del 1 al 10 se escribe con letras, el signo % va separado como en 14%, y los millares 1,000 o 10.000, los decimales van con punto o coma: 1.345. No es décimo primero, ni doceavo, ni décimo tercero. 40 mil litros. El 10 de agosto del 2022. No es Junio ni Miércoles. En lugar de --, poner raya.\nA: ¿Por qué no iba de hacerlo? «Este es un texto con comillas españolas» —¿Estará consultando las dos obras que le dije? —No parece, porque no cambia la abreviatura de D.ª, ¿o sí? Érase una mañana fría y gris... Caperucita le dijo a su mamá: «Voy a llevarle su comida a mi abuela». Me dijo que no era cierto. La convenció de que viniera con nosotros. Le dijo que no quería comer chocolate. «Solo» nunca lleva tilde, según las nuevas normas. Necesito que me dé dinero. Para asistir el día de mañana, 24 de marzo, a las 8:50 a. m., haz clic en el siguiente botón. Creo que, tarde o temprano, cederá. Del uno al diez se escribe con letras; el signo % va separado, como en 14 %, y los millares, 1000 o 10 000. Los decimales van con punto o coma: 1.345. No es undécimo, ni duodécimo, ni décimo tercero. 40 000 litros. El 10 de agosto de 2022. No es junio ni miércoles. En lugar de —, poner raya.\n###\nQ: que me dijo?\nQue pusiera rayas.\nDe acuerdo –respondió el primero.\nA: ¿Qué me dijo?\n—Que pusiera rayas.\n—De acuerdo —respondió el primero.\n###\n",
  temperature=0,
  max_tokens=804,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["###"]
)
