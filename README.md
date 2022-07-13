# FINAL_SI

## API

Primero se inicia la API para que se se hagan los GET y POST request.

```bash
$ python server.py
```

## Publisher

Esta clase se encarga de hacer los POST hacia la API con el message y el 
topic que se le inserta por *input*, retorna el status de nuestro request {200 o 401}:

```bash
$ python publisher.py
```

## Subscriber

Esta clase se encarga de hacer los GET hacia la API con el 
topic que se le inserta por *input*, retorna los messages en formato json:

```bash
$ python subscriber.py
```

## JMeter


