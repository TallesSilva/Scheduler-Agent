# 📆 Scheduler Agent

Implementa uma interface conversacional que confirma visitas técnicas de um departamento de implantanção de serviços de telecomunicações. A partir de um conjunto de visitas agendadas i.e. timetable, é orquestrado o contato a todos os usuários

## Set-up

Para o desenvolvimento e uso local, recomenda-se o uso de ambientes virtuais (`conda`, `virtualenv`):

``` bash
conda create -n scheduler python=3.6
conda activate scheduler
pip install rasa==1.2.3
```

### Treinamento

Para treinar os modelos:

``` bash
rasa train
```


### Uso

Para conversar com o agente:

``` bash
rasa shell
```