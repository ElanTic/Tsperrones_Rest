CREATE TABLE pertenencia (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dueno VARCHAR(30),
    nombre VARCHAR(50),
    categoria VARCHAR(50),
    marca VARCHAR(50),
    modelo VARCHAR(50),
    color VARCHAR(50), -- Assuming color is represented as a string
    descripcion VARCHAR(255), -- Allowing for longer string
    foto VARCHAR(255) -- Assuming foto is represented as a URL
);

-- Adding foreign key constraint
ALTER TABLE pertenencia
ADD FOREIGN KEY (dueno) REFERENCES joven_0(nombre);
