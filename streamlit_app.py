import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt="Corrija la escritura.\n\nno le dijo \"nada\" sino que se fue entonces comprendió que sería inútil\n\nNo le dijo «nada»; sino que se fue. Entonces comprendió que sería inútil.\n###\nPor qué será que lo rechazó Es interesante.\n\n¿Por qué será que lo rechazó? Es interesante.\n###\n--qué le dije?\n-que cambiara los guiones,\n\n—¿Qué le dije?\n—Que cambiara los guiones.\n###\nno se si cambiaara o si mejorará el texto lo unico que sé es que el anterior funcionaba bien. verdad?\n--si, correcto.\n\nNo sé si cambiará o si mejorará el texto; lo único que sé es que el anterior funcionaba bien. ¿Verdad?\n—Sí, correcto.\n###\nesta es una prueba se espera que ponga `punto que corrija \"las comillas\".\n--y los guiones! tambien los signos de interrogación?\n\nEsta es una prueba; se espera que ponga «punto» que corrija «las comillas».\n—¡Y los guiones! ¿También los signos de interrogación?\n###",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
