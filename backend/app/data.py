# Horarios compartidos por colaborador local el 18/11/2026; pendientes de validación parroquial.
CHURCHES = [
    {
        "id": 1,
        "name": "Parroquia La Sagrada Familia",
        "city": "San Miguel",
        "department": "San Miguel",
        "address": "Colonia Belén, San Miguel, El Salvador",
        "phone": "2661-4298",
        "verified": False,
        "schedule_status": "community_reported",
        "schedule_note": "Horario aportado por un colaborador local; confirmar con secretaría.",
        "chapel": True,
        "source_url": "https://diocesisdesanmiguelsv.org/vicaria-san-miguel-arcangel/",
        "masses": [
            {"days": "Martes a sábado", "times": ["18:00"]},
            {"days": "Domingo", "times": ["06:00", "10:00", "18:00"]},
        ],
    },
    {
        "id": 2,
        "name": "Catedral Basílica Reina de la Paz",
        "city": "San Miguel",
        "department": "San Miguel",
        "address": "Barrio El Centro, San Miguel, El Salvador",
        "phone": "2661-1979",
        "verified": False,
        "schedule_status": "broadcast_reported",
        "schedule_note": "Transmisiones publicadas en octubre de 2026. Un colaborador menciona una posible misa presencial dominical a las 16:00, todavía sin confirmar. Consultar con la Catedral antes de asistir.",
        "unconfirmed_masses": [{"days": "Domingo (posible misa presencial)", "times": ["16:00"]}],
        "chapel": False,
        "source_url": "https://santuariosenvivo.com/catedral-de-san-miguel/",
        "masses": [
            {"days": "Lunes a sábado (transmisiones)", "times": ["07:00", "16:00"]},
            {"days": "Domingo (transmisión)", "times": ["09:00"]},
        ],
    },
]
