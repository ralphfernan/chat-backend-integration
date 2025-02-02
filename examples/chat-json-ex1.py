#pydantic
class Country(BaseModel):
  name: str
  capital: str
  languages: list[str]

#ollama
response = chat(
  messages=[
    {
      'role': 'user',
      'content': 'Give me details about China.',
    }
  ],
  model='mistral-small',
  #Uncomment format line below for json output, e.g. name='search' capital='Washington D.C.' languages=['English']  
  format=Country.model_json_schema(),
)

country = Country.model_validate_json(response.message.content)
print(country)
#print(response.message.content)