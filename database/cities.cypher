// ------------------------------------------------------------------------------
// Load/Update Cities
// ------------------------------------------------------------------------------
CALL apoc.load.json("http://api.almundo.it:8080/api/catalog/cities") YIELD value

WITH value as cities
WHERE NOT cities.iata_code = ''
WITH cities.id as id, cities.iata_code as iata_code, cities.name.es as name

MERGE (c:City {_id: id}) ON CREATE SET c.iata_code = iata_code, c.name = name
// ------------------------------------------------------------------------------
//
// 
//
//
// ------------------------------------------------------------------------------
// Load/Update Countries
// ------------------------------------------------------------------------------
CALL apoc.load.json("http://api.almundo.it:8080/api/catalog/countries") YIELD value

WITH value as cities
WHERE NOT cities.iata_code = ''
WITH cities.id as id, cities.iata_code as iata_code, cities.name.es as name

MERGE (c:City {_id: id}) ON CREATE SET c.iata_code = iata_code, c.name = name
