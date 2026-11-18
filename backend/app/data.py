from dataclasses import dataclass

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
        "schedule_status": "pending",
        "schedule_note": "Horarios de misa pendientes de confirmar con la catedral.",
        "chapel": False,
        "source_url": "https://diocesisdesanmiguelsv.org/vicaria-reina-de-la-paz/",
        "masses": [],
    },
]
