CREATE TABLE ficha_objeto_p (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date_found DATETIME,
    date_lost DATETIME,
    ubicacion VARCHAR(255),
    is_found BOOLEAN,
    owner_id VARCHAR(30), -- Assuming owner_id is a string
    pertenencia_id INT,  -- Assuming pertenencia_id is an integer
    
    -- Adding foreign key constraints
    FOREIGN KEY (owner_id) REFERENCES joven_0(nombre),
    FOREIGN KEY (pertenencia_id) REFERENCES pertenencia(id)
);
