RENAME TABLE crud_ciudad TO crud_dpto;

ALTER TABLE crud_dpto
DROP COLUMN descripcion;


INSERT INTO `crud_dpto` (`id`, `nombre`) VALUES
('1', 'Amazonas'),
('2', 'Antioquia'),
('3', 'Arauca'),
('4', 'Atlántico'),
('5', 'Bolívar'),
('6', 'Boyacá'),
('7', 'Caldas'),
('8', 'Caquetá'),
('9', 'Casanare'),
('10', 'Cauca'),
('11', 'Cesar'),
('12', 'Chocó'),
('13', 'Cundinamarca'),
('14', 'Córdoba'),
('15', 'Guainía'),
('16', 'Guaviare'),
('17', 'Huila'),
('18', 'La Guajira'),
('19', 'Magdalena'),
('20', 'Meta'),
('21', 'Nariño'),
('22', 'Norte de Santander'),
('23', 'Putumayo'),
('24', 'Quindío'),
('25', 'Risaralda'),
('26', 'San Andrés y Providencia'),
('27', 'Santander'),
('28', 'Sucre'),
('29', 'Tolima'),
('30', 'Valle del Cauca'),
('31', 'Vaupés'),
('32', 'Vichada');


INSERT INTO `crud_tipodocumento` (`id`, `nombre`, `descripcion`) VALUES
('1', 'TI', 'Tarjeta de Identidad'),
('2', 'CC', 'Cedula de Ciudadania'),
('3', 'CE', 'Cedula de Extranjeria'),
('4', 'PA', 'Pasaporte');


SELECT * FROM crud_dpto;
SELECT * FROM crud_persona;
SELECT * FROM crud_tipodocumento;