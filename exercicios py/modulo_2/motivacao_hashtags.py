#você trabalha como analista de dados de mídias sociais e precisa
#descobrir todas as hashtags qua alcançaram o top trending do twitter
#durante uma semana:

  hashtags_seg = ['#ttblue', '#monica','#dinossauro']
  hashtags_ter = ['#uva', '#ttblue', 'brasil']
  hashtags_qua = ['#SãoPaulo', '#freeDonuts', '#BK']
  hashtags_qui = ['#ttblue', '#waterbomb', '#threads']
  hashtags_sex = ['#R&B', '#haikyuu', '#threads']

#uma simples concatenação de listas fará om que a hashtag #ttblue, entre outras,
#aparecça mais de uma vez.

  hashtags_semana = hashtags_seg + hashtags_ter + hashtags_qua + hashtags_qui + hashtags_sex
  print(hashtags_semana)

#para uma análise de dados mais precisa, é necessário remover elementos repetidos

  print(len(hashtags_semana))
  hashtags_semana = list(set(hashtags_seg + hashtags_ter + hashtags_qua + hashtags_qui + hashtags_sex))
  print(hashtags_semana)
  print(len(hashtags_semana))
