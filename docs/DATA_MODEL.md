# Modelo de datos inicial

## Entidades
- **Country**: id, name, iso_code.
- **AdministrativeArea**: id, country_id, parent_id, name, type (departamento, municipio, distrito u otro).
- **Church**: id, name, type (parroquia, capilla, catedral, etc.), area_id, address, latitude, longitude, phone, website, status.
- **Schedule**: id, church_id, kind (misa, confesión, adoración), weekday, start_time, end_time, notes, valid_from, valid_until, verification_status, verified_at.
- **Source**: id, church_id, schedule_id (opcional), url, publisher, checked_at, notes.

## Reglas
1. No publicar horarios sin respaldo o verificación.
2. Mostrar la fecha de última verificación y un aviso de posibles cambios.
3. Teléfono y coordenadas son opcionales hasta su comprobación.
4. Separar iglesia y capilla como tipos de lugar; permitir varias celebraciones por día.
5. Preparar la jerarquía territorial para múltiples países.
6. No exigir cuentas para consultar datos.
