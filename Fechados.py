from datetime import datetime, timedelta

def calcular_limite_zona(fecha_inicio, valor, unidad, modo_inicio="mismo_dia"):
    """Calcula la fecha/hora límite según los días, horas o regla de 11:59 p.m."""
    if valor == 0 or valor is None:
        return None

    if unidad == "horas":
        return fecha_inicio + timedelta(hours=valor)
        
    elif unidad == "cierre_dia":  # Regla especial 11:59 p.m.
        dias_a_sumar = valor if modo_inicio == "siguiente_dia" else (valor - 1)
        fecha_fin = fecha_inicio + timedelta(days=dias_a_sumar)
        return fecha_fin.replace(hour=23, minute=59, second=0, microsecond=0)
        
    elif unidad == "dias":
        if modo_inicio == "siguiente_dia":
            return fecha_inicio + timedelta(days=valor)
        else:
            return fecha_inicio + timedelta(days=valor - 1)
            
    return fecha_inicio


# -------------------------------------------------------------------
# BASE DE DATOS EXTRAÍDA DE LA TABLA DE VIDA ÚTIL 2026
# -------------------------------------------------------------------
productos = [
    # --- TROZOS Y CÁRNICOS ---
    {
        "id": 1,
        "nombre": "Alitas de pollo-local",
        "vigencia": {
            "recibido": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
            },
            "preparado": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría o Makeline inferior",
            },
            "en_linea": {
                "valor": 24,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 2,
        "nombre": "Poppers de pollo",
        "vigencia": {
            "recibido": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
            },
            "preparado": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría o Makeline inferior",
            },
            "en_linea": {
                "valor": 24,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 3,
        "nombre": "Chicken Tender",
        "vigencia": {
            "recibido": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
            },
            "preparado": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría o Makeline inferior",
            },
            "en_linea": {
                "valor": 24,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 4,
        "nombre": "Pollo asado-importado",
        "vigencia": {
            "recibido": {
                "valor": 10,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
            },
            "preparado": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría o Makeline inferior",
            },
            "en_linea": {
                "valor": 24,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 5,
        "nombre": "Salchicha italiana",
        "vigencia": {
            "recibido": {
                "valor": 12,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
            },
            "preparado": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría o Makeline inferior",
            },
            "en_linea": {
                "valor": 24,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 6,
        "nombre": "Chorizo-local",
        "vigencia": {
            "recibido": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
            },
            "preparado": {
                "valor": 4,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría o Makeline inferior",
            },
            "en_linea": {
                "valor": 24,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 7,
        "nombre": "Chorizo Parrillero",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
                "empaque": "Caduca según la fecha impresa en el empaque original",
            },
            "preparado": {
                "valor": 4,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría o Makeline inferior",
            },
            "en_linea": {
                "valor": 24,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 8,
        "nombre": "Carne de res-local",
        "vigencia": {
            "recibido": {
                "valor": 12,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
            },
            "preparado": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría o Makeline inferior",
            },
            "en_linea": {
                "valor": 48,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 9,
        "nombre": "Salchicha de cerdo",
        "vigencia": {
            "recibido": {
                "valor": 12,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
            },
            "preparado": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría o Makeline inferior",
            },
            "en_linea": {
                "valor": 48,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 10,
        "nombre": "Tocino",
        "vigencia": {
            "recibido": {
                "valor": 30,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
            },
            "preparado": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría o Makeline inferior",
            },
            "en_linea": {
                "valor": 48,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 11,
        "nombre": "Pepperoni de cerdo",
        "vigencia": {
            "recibido": {
                "valor": 30,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
            },
            "preparado": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría o Makeline inferior",
            },
            "en_linea": {
                "valor": 48,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 12,
        "nombre": "Jamón local",
        "vigencia": {
            "recibido": {
                "valor": 14,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
            },
            "preparado": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría o Makeline inferior",
            },
            "en_linea": {
                "valor": 48,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    # --- QUESOS ---
    {
        "id": 13,
        "nombre": "Queso Mozzarella",
        "vigencia": {
            "recibido": {
                "valor": 14,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
            },
            "preparado": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría o Makeline inferior",
            },
            "en_linea": {
                "valor": 24,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 14,
        "nombre": "Queso en tiras",
        "vigencia": {
            "recibido": {
                "valor": 14,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
            },
            "preparado": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría o Makeline inferior",
            },
            "en_linea": {
                "valor": 24,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 15,
        "nombre": "Queso cheddar en tiras",
        "vigencia": {
            "recibido": {
                "valor": 60,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
            },
            "preparado": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría o Makeline inferior",
            },
            "en_linea": {
                "valor": 24,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 16,
        "nombre": "Queso cheddar rayado",
        "vigencia": {
            "recibido": {
                "valor": 60,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
            },
            "preparado": {
                "valor": 5,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría o Makeline inferior",
            },
            "en_linea": {
                "valor": 24,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 17,
        "nombre": "Salsa de queso cheddar",
        "vigencia": {
            "recibido": {
                "valor": 90,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
            },
            "preparado": {
                "valor": 5,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
            "en_linea": {
                "valor": 24,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 18,
        "nombre": "Mezcla de 3 quesos (Asiago, Fontina, Provolone)",
        "vigencia": {
            "recibido": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
            },
            "preparado": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría o Makeline inferior",
            },
            "en_linea": {
                "valor": 24,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 19,
        "nombre": "Mezcla de 2 quesos (Romano y Parmesano)",
        "vigencia": {
            "recibido": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
            },
            "preparado": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría o Makeline inferior",
            },
            "en_linea": {
                "valor": 24,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    # --- VEGETALES Y FRUTAS ---
    {
        "id": 20,
        "nombre": "Champiñón",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
            "preparado": {
                "valor": 24,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría o Makeline inferior",
            },
            "en_linea": {
                "valor": 1,
                "unidad": "cierre_dia",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 21,
        "nombre": "Cebolla blanca",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
            "preparado": {
                "valor": 2,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría o Makeline inferior",
            },
            "en_linea": {
                "valor": 1,
                "unidad": "cierre_dia",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 22,
        "nombre": "Cebolla roja",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
            "preparado": {
                "valor": 2,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría o Makeline inferior",
            },
            "en_linea": {
                "valor": 1,
                "unidad": "cierre_dia",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 23,
        "nombre": "Pimiento rojo",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
            "preparado": {
                "valor": 2,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría o Makeline inferior",
            },
            "en_linea": {
                "valor": 1,
                "unidad": "cierre_dia",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 24,
        "nombre": "Pimiento verde",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
            "preparado": {
                "valor": 2,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría o Makeline inferior",
            },
            "en_linea": {
                "valor": 1,
                "unidad": "cierre_dia",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 25,
        "nombre": "Tomate",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
            "preparado": {
                "valor": 2,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría o Makeline inferior",
            },
            "en_linea": {
                "valor": 1,
                "unidad": "cierre_dia",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 26,
        "nombre": "Jalapeños",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
            "preparado": {
                "valor": 60,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
            "en_linea": {
                "valor": 1,
                "unidad": "cierre_dia",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 27,
        "nombre": "Aceituna negra",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
            "preparado": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
            "en_linea": {
                "valor": 48,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 28,
        "nombre": "Aceituna verde",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
            "preparado": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
            "en_linea": {
                "valor": 48,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 29,
        "nombre": "Piña - lata",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
            "preparado": {
                "valor": 15,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
            "en_linea": {
                "valor": 48,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 30,
        "nombre": "Pepperoncini / Banana Peppers",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
            "preparado": {
                "valor": 15,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
            "en_linea": {
                "valor": 1,
                "unidad": "cierre_dia",
                "inicio": "mismo_dia",
                "almacenamiento": "Temperatura ambiente/ Makeline",
            },
        },
    },
    # --- SALSAS ---
    {
        "id": 31,
        "nombre": "Salsa pizza lata",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en la lata",
            },
            "preparado": {
                "valor": 10,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
            "en_linea": {
                "valor": 10,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 32,
        "nombre": "Salsa de mayonesa con ají limo",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
            "preparado": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
            "en_linea": {
                "valor": 1,
                "unidad": "cierre_dia",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 33,
        "nombre": "Salsa rosada (0.5 kg / 1 kg)",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en la bolsa",
            },
            "preparado": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
            "en_linea": {
                "valor": 1,
                "unidad": "cierre_dia",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 34,
        "nombre": "Salsa Parrillera",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
            "preparado": {
                "valor": 3,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
            "en_linea": {
                "valor": 1,
                "unidad": "cierre_dia",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 35,
        "nombre": "Salsa de ajo (botella-granel)",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en la botella",
            },
            "preparado": {
                "valor": 21,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
            "en_linea": {
                "valor": 1,
                "unidad": "cierre_dia",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 36,
        "nombre": "Salsa de mango habanero (bolsa)",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en la bolsa",
            },
            "preparado": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
            "en_linea": {
                "valor": 1,
                "unidad": "cierre_dia",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 37,
        "nombre": "Salsa Ranch",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
                "empaque": "Caduca según la fecha impresa en la bolsa",
            },
            "preparado": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
            "en_linea": {
                "valor": 1,
                "unidad": "cierre_dia",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 38,
        "nombre": "Salsa Bechamel",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
                "empaque": "Caduca según la fecha impresa en la bolsa",
            },
            "preparado": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
            "en_linea": {
                "valor": 1,
                "unidad": "cierre_dia",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 39,
        "nombre": "Salsa Chimichurri",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
                "empaque": "Caduca según la fecha impresa en la bolsa",
            },
            "preparado": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
            "en_linea": {
                "valor": 1,
                "unidad": "cierre_dia",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 40,
        "nombre": "Salsa de ajo (blister cup)",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en el blister",
            },
            "preparado": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en el blister",
            },
            "en_linea": {
                "valor": 1,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Temperatura ambiente",
            },
        },
    },
    {
        "id": 41,
        "nombre": "Salsa Parmesana (botella granel)",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
            "preparado": {
                "valor": 21,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
            "en_linea": {
                "valor": 1,
                "unidad": "cierre_dia",
                "inicio": "mismo_dia",
                "almacenamiento": "Temperatura ambiente",
            },
        },
    },
    {
        "id": 42,
        "nombre": "Salsa BBQ (bolsa)",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en la bolsa",
            },
            "preparado": {
                "valor": 4,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
            "en_linea": {
                "valor": 48,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Temperatura ambiente",
            },
        },
    },
    {
        "id": 43,
        "nombre": "Salsa BBQ (blister cup)",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en el blister",
            },
            "preparado": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en el blister",
            },
            "en_linea": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
                "empaque": "Caduca según la fecha impresa en el blister",
            },
        },
    },
    {
        "id": 44,
        "nombre": "Salsa Buffalo (blister cup)",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en el blister",
            },
            "preparado": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en el blister",
            },
            "en_linea": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
                "empaque": "Caduca según la fecha impresa en el blister",
            },
        },
    },
    {
        "id": 45,
        "nombre": "Salsa de Miel Picante",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
            "preparado": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
            "en_linea": {
                "valor": 1,
                "unidad": "cierre_dia",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    # --- INSUMOS Y MASAS ---
    {
        "id": 46,
        "nombre": "Dustinator",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
                "empaque": "Caduca según la fecha impresa en el saco",
            },
            "preparado": {
                "valor": 14,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
            "en_linea": {
                "valor": 48,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Temperatura ambiente",
            },
        },
    },
    {
        "id": 47,
        "nombre": "Masa Croissant",
        "vigencia": {
            "recibido": {
                "valor": 5,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
            },
            "preparado": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
                "empaque": "Uso inmediato tras descongelar",
            },
            "en_linea": {
                "valor": 1,
                "unidad": "cierre_dia",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 48,
        "nombre": "Masa delgada importada",
        "vigencia": {
            "recibido": {
                "valor": 30,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
            },
            "preparado": {
                "valor": 3,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
        },
    },
    {
        "id": 49,
        "nombre": "Azúcar glaseada (Icing) - local",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
                "empaque": "Caduca según la fecha impresa en el sachet/bolsa",
            },
            "preparado": {
                "valor": 30,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
            "en_linea": {
                "valor": 48,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Temperatura ambiente",
            },
        },
    },
    {
        "id": 50,
        "nombre": "Masa Pan Pizza / Pan de ajo",
        "vigencia": {
            "recibido": {
                "valor": 3,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
            },
            "preparado": {
                "valor": 2,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
            "en_linea": {
                "valor": 8,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Temperatura ambiente",
            },
        },
    },
    {
        "id": 51,
        "nombre": "Orégano (sachet o granel)",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en el sachet/bolsa",
            },
            "preparado": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
            "en_linea": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
        },
    },
    {
        "id": 52,
        "nombre": "Ají panca (sachet o granel)",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en el sachet/bolsa",
            },
            "preparado": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
            "en_linea": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
        },
    },
    # --- OTROS Y PREPARACIONES (PREPS) ---
    {
        "id": 53,
        "nombre": "Pasta de lasagna",
        "vigencia": {
            "recibido": {
                "valor": 10,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
            },
            "preparado": {
                "valor": 8,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
            "en_linea": {
                "valor": 1,
                "unidad": "cierre_dia",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 54,
        "nombre": "Tortilla",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
            "preparado": {
                "valor": 7,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
            "en_linea": {
                "valor": 1,
                "unidad": "cierre_dia",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 55,
        "nombre": "Manjar Blanco",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en la manga/bolsa",
            },
            "preparado": {
                "valor": 30,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Almacén seco",
            },
            "en_linea": {
                "valor": 5,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 56,
        "nombre": "Azúcar Impalpable",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
            "preparado": {
                "valor": 30,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Almacén seco",
            },
            "en_linea": {
                "valor": 5,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Temperatura ambiente",
            },
        },
    },
    {
        "id": 57,
        "nombre": "Aceite",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
            "preparado": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
            "en_linea": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
        },
    },
    {
        "id": 58,
        "nombre": "Sal",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
            "preparado": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
            "en_linea": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
        },
    },
    {
        "id": 59,
        "nombre": "Pasta Rigatoni",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
            "preparado": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
            "en_linea": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Almacén seco",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
        },
    },
    {
        "id": 60,
        "nombre": "Masa pan",
        "vigencia": {
            "recibido": {
                "valor": 10,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
            },
            "preparado": {
                "valor": 10,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
            "en_linea": {
                "valor": 10,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 61,
        "nombre": "Lasagna All the meats",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "N/A",
                "empaque": "Elaborado en tienda",
            },
            "preparado": {
                "valor": 4,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
        },
    },
    {
        "id": 62,
        "nombre": "Lasagna The Works",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "N/A",
                "empaque": "Elaborado en tienda",
            },
            "preparado": {
                "valor": 4,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
            "en_linea": {
                "valor": 4,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 63,
        "nombre": "Lasagna Americana",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "N/A",
                "empaque": "Elaborado en tienda",
            },
            "preparado": {
                "valor": 4,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
            "en_linea": {
                "valor": 4,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 64,
        "nombre": "Rollitos Pepperoni",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "N/A",
                "empaque": "Elaborado en tienda",
            },
            "preparado": {
                "valor": 6,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline / Mantenedor",
            },
            "en_linea": {
                "valor": 6,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 65,
        "nombre": "Rollitos Jamón",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "N/A",
                "empaque": "Elaborado en tienda",
            },
            "preparado": {
                "valor": 6,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline / Mantenedor",
            },
            "en_linea": {
                "valor": 6,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 66,
        "nombre": "Rollitos Manjar",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "N/A",
                "empaque": "Elaborado en tienda",
            },
            "preparado": {
                "valor": 6,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline / Mantenedor",
            },
            "en_linea": {
                "valor": 6,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 67,
        "nombre": "Rollitos Canela",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "N/A",
                "empaque": "Elaborado en tienda",
            },
            "preparado": {
                "valor": 6,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline / Mantenedor",
            },
            "en_linea": {
                "valor": 6,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 68,
        "nombre": "Pasta Chicken",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "N/A",
                "empaque": "Elaborado en tienda",
            },
            "preparado": {
                "valor": 2,
                "unidad": "cierre_dia",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
            "en_linea": {
                "valor": 2,
                "unidad": "cierre_dia",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 69,
        "nombre": "Pasta Bolognesa",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "N/A",
                "empaque": "Elaborado en tienda",
            },
            "preparado": {
                "valor": 2,
                "unidad": "cierre_dia",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
            "en_linea": {
                "valor": 2,
                "unidad": "cierre_dia",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
    {
        "id": 70,
        "nombre": "Piña - bolsa",
        "vigencia": {
            "recibido": {
                "valor": 0,
                "unidad": "dias",
                "inicio": "siguiente_dia",
                "almacenamiento": "Cámara fría",
                "empaque": "Caduca según la fecha impresa en el empaque",
            },
            "preparado": {
                "valor": 15,
                "unidad": "dias",
                "inicio": "mismo_dia",
                "almacenamiento": "Cámara fría",
            },
            "en_linea": {
                "valor": 48,
                "unidad": "horas",
                "inicio": "mismo_dia",
                "almacenamiento": "Makeline",
            },
        },
    },
]


from datetime import datetime, timedelta


def calcular_vencimiento_detallado(vigencia, fecha_base):
    valor = vigencia.get("valor", 0)
    unidad = vigencia.get("unidad", "dias")
    inicio = vigencia.get("inicio", "mismo_dia").replace("_", " ")

    # Si depende de la fecha impresa
    if valor == 0 and "empaque" in vigencia:
        return f"{vigencia['empaque']}"

    # Ajuste de fecha según el tipo de inicio
    base_calculo = fecha_base
    if inicio == "siguiente dia" and unidad == "dias":
        # Se empieza a contar desde el día siguiente
        base_calculo = fecha_base + timedelta(days=1)

    # Cálculo final
    if unidad == "horas":
        fecha_venc = base_calculo + timedelta(hours=valor)
        str_fecha = fecha_venc.strftime("%d/%m/%Y a las %H:%M hs")
    elif unidad == "dias":
        fecha_venc = base_calculo + timedelta(days=valor)
        str_fecha = fecha_venc.strftime("%d/%m/%Y")
    elif unidad == "cierre_dia":
        fecha_venc = base_calculo + timedelta(days=valor)
        str_fecha = fecha_venc.strftime("%d/%m/%Y (Al cierre)")
    else:
        str_fecha = "Fecha N/A"

    return f"{str_fecha} ({valor} {unidad}) ({inicio})"


from datetime import datetime, timedelta


def calcular_vencimiento_detallado(datos_etapa, fecha_eval):
    valor = datos_etapa.get("valor", 0)
    unidad = datos_etapa.get("unidad", "dias")
    inicio = datos_etapa.get("inicio", "mismo_dia")

    # Si es fecha según empaque
    if valor == 0 or "empaque" in datos_etapa:
        return datos_etapa.get("empaque", "Ver indicación en empaque")

    fecha_venc = calcular_limite_zona(fecha_eval, valor, unidad, inicio)

    if fecha_venc is None:
        return datos_etapa.get("empaque", "Ver indicación en empaque")

    # Formateo amigable según la unidad
    if unidad == "horas":
        txt_inicio = inicio.replace("_", " ")
        return f"{fecha_venc.strftime('%d/%m/%Y a las %H:%M hs')} ({valor} horas) ({txt_inicio})"

    elif unidad == "cierre_dia":
        return f"{fecha_venc.strftime('%d/%m/%Y a las 23:59 hs')} (Al cierre del día)"

    else:  # dias
        txt_inicio = inicio.replace("_", " ")
        return f"{fecha_venc.strftime('%d/%m/%Y')} ({valor} días) ({txt_inicio})"


def imprimir_ficha_producto(lista_productos, id_producto, fecha_eval=None):
    if fecha_eval is None:
        fecha_eval = datetime.now()

    # Buscar el producto
    producto = next(
        (p for p in lista_productos if p["id"] == id_producto), None
    )

    if not producto:
        print(f"❌ No se encontró el producto con ID {id_producto}")
        return

    nombre = producto["nombre"].upper()
    vig = producto["vigencia"]

    # Formatear salida
    print("==========================================================")
    print(f"📦 FICHA DEL PRODUCTO #{producto['id']}: {nombre}")
    print(
        f"   Fecha de evaluación: {fecha_eval.strftime('%d/%m/%Y %H:%M hs')}"
    )
    print("==========================================================")

    # Recibido
    if "recibido" in vig:
        r = vig["recibido"]
        venc_r = calcular_vencimiento_detallado(r, fecha_eval)
        print(f"  📥 Recibido  : ({r.get('almacenamiento', 'N/A')})")
        print(f"     -> Vence el: {venc_r}")

    # Preparado
    if "preparado" in vig:
        p = vig["preparado"]
        venc_p = calcular_vencimiento_detallado(p, fecha_eval)
        print(f"  👨‍🍳 Preparado : ({p.get('almacenamiento', 'N/A')})")
        print(f"     -> Vence el: {venc_p}")

    # En línea
    if "en_linea" in vig:
        l = vig["en_linea"]
        venc_l = calcular_vencimiento_detallado(l, fecha_eval)
        print(f"  🌐 En línea  : ({l.get('almacenamiento', 'N/A')})")
        print(f"     -> Vence el: {venc_l}")

    print("----------------------------------------------------------\n")

def buscar_y_mostrar_producto(fecha_base=None):
    if fecha_base is None:
        fecha_base = datetime.now()

    busqueda = input("\n🔍 Ingresa el nombre del producto a buscar: ").strip().lower()
    
    # 1. Filtramos los productos que coinciden
    coincidencias = [p for p in productos if busqueda in p["nombre"].lower()]
    
    if not coincidencias:
        print("❌ No se encontraron productos con ese nombre.")
        return

    # 2. Si solo hay 1 coincidencia, lo seleccionamos automáticamente
    if len(coincidencias) == 1:
        producto_seleccionado = coincidencias[0]
    else:
        # Si hay más de 1, mostramos la lista numerada para que elijas
        print(f"\n✅ Se encontraron {len(coincidencias)} coincidencias:")
        for indice, prod in enumerate(coincidencias, start=1):
            print(f"  {indice}. {prod['nombre']}")
        
        while True:
            try:
                eleccion = int(input(f"\nSelecciona el número del producto (1-{len(coincidencias)}): "))
                if 1 <= eleccion <= len(coincidencias):
                    # Guardamos el producto elegido (restamos 1 porque las listas en Python empiezan en 0)
                    producto_seleccionado = coincidencias[eleccion - 1]
                    break
                else:
                    print(f"❌ Número fuera de rango. Ingresa un valor entre 1 y {len(coincidencias)}.")
            except ValueError:
                print("❌ Entrada inválida. Ingresa solo el número.")

    # 3. Imprimimos ÚNICAMENTE la ficha del producto seleccionado
    # (Usa aquí el mismo formato de impresión que ya tenías)
    # En la línea 1868 cambia esto:
    imprimir_ficha_producto(productos, producto_seleccionado["id"], fecha_base)

def menu_principal():
    while True:
        print("\n=== SISTEMA DE CONSULTA DE PRODUCTOS (VIDA ÚTIL 2026) ===")
        print("1. Consultar fechado de hoy")
        print("2. Consultar con otra fecha")
        print("3. Minijuego de rotulado")
        print("4. Salir")
        
        opcion = input("\nElige una opción (1-4): ").strip()
        
        if opcion == "1":
            buscar_y_mostrar_producto()
            
        elif opcion == "2":
            try:
                anio = int(input("Año (ej. 2026): "))
                mes = int(input("Mes (1-12): "))
                dia = int(input("Día (1-31): "))
                buscar_y_mostrar_producto(fecha_base=datetime(anio, mes, dia, 12, 0))
            except ValueError:
                print("❌ Fecha inválida.")
                
        elif opcion == "3":
            minijuego_fechado(productos)
            
        elif opcion == "4":
            print("¡Hasta luego!")
            break
            
        else:
            print("❌ Opción no válida, intenta de nuevo.")

import random


def minijuego_fechado(productos):
    puntaje = 0
    juego_activo = True

    print("\n" + "=" * 50)
    print("🎮 ¡BIENVENIDO AL MINIJUEGO DE ROTULADO Y FECHADO! 🎮")
    print("Regla: Responde con el número de días u horas correspondiente.")
    print(
        "💡 NOTA: Los productos con fecha 'según empaque', 'vigencia 'al cierre del día' o 'Elaborado en tienda' se marcan con 0."
    )
    print("Si cometes un solo error... ¡GAME OVER!")
    print("=" * 50 + "\n")

    while juego_activo:
        producto = random.choice(productos)
        nombre = producto["nombre"]
        vigencia = producto["vigencia"]

        print(f"📌 PUNTAJE ACTUAL: {puntaje}")
        print(f"👉 Producto a evaluar: *** {nombre.upper()} ***\n")

        estados = [
            ("recibido", "1. ¿Cuántos DÍAS de vigencia tiene en RECIBIDO? "),
            ("preparado", "2. ¿Cuántos DÍAS de vigencia tiene en PREPARADO? "),
            (
                "en_linea",
                "3. ¿Cuántas HORAS (o días) de valor tiene EN LÍNEA? ",
            ),
        ]

        for clave_estado, pregunta in estados:
            if clave_estado not in vigencia:
                continue

            try:
                respuesta_usuario = int(input(pregunta))
            except ValueError:
                print("❌ Entrada inválida. Debes ingresar un número entero.")
                juego_activo = False
                break

            datos_estado = vigencia[clave_estado]
            unidad_correcta = datos_estado.get("unidad", "dias")
            val_real = datos_estado.get("valor", 0)

            # Determinamos el motivo del 0 si aplica
            motivo_cero = ""
            if unidad_correcta == "cierre_dia":
                valor_esperado = 0
                motivo_cero = "(Es 0 porque su vigencia es al CIERRE DEL DÍA)"
            elif val_real == 0 or "empaque" in datos_estado:
                valor_esperado = 0
                detalle_empaque = datos_estado.get(
                    "empaque", "Según empaque/tienda"
                )
                motivo_cero = (
                    f"(Es 0 porque aplica fecha de EMPAQUE: '{detalle_empaque}')"
                )
            else:
                valor_esperado = val_real

            if respuesta_usuario == valor_esperado:
                # Construimos la aclaración pedagógica si la respuesta fue 0
                if valor_esperado == 0:
                    if unidad_correcta == "cierre_dia":
                        aclaracion = " (Al cierre del día)"
                    elif "empaque" in datos_estado:
                        aclaracion = f" ({datos_estado['empaque']})"
                    else:
                        aclaracion = " (Según empaque / Elaborado en tienda)"
                else:
                    aclaracion = ""

                print(f"   ¡Correcto! ✅{aclaracion}\n")
            else:
                print("\n" + "❌" * 25)
                print(f"¡INCORRECTO! Te equivocaste en '{clave_estado}'.")
                print(f"Tu respuesta: {respuesta_usuario}")
                print(f"Valor correcto: {valor_esperado}")

                # Si la respuesta era 0, mostramos la razón pedagógica
                if valor_esperado == 0 and motivo_cero:
                    print(f"📌 Explicación: {motivo_cero}")
                else:
                    print(
                        f"📌 Detalle original: {val_real} {unidad_correcta}"
                    )

                print("❌" * 25)
                juego_activo = False
                break

        if juego_activo:
            puntaje += 30
            print(
                f"🎉 ¡Súper! Has completado la ficha de '{nombre}'. Sumas 30 puntos.\n"
            )
            print("-" * 50)

    print("\n" + "=" * 50)
    print("🏁 GAME OVER - JUEGO TERMINADO 🏁")
    print(f"🏆 Puntaje total conseguido: {puntaje} punto(s)")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    menu_principal()