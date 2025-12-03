Prompt: sql to create a database called blog with table blog insert several articles in spanish

-- Crear base de datos
CREATE DATABASE IF NOT EXISTS blogphp;
USE blogphp;

-- Tabla: blog (artículos del blog)
CREATE TABLE IF NOT EXISTS blog (
    id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(200) NOT NULL,
    contenido TEXT NOT NULL,
    autor VARCHAR(100) NOT NULL,
    fecha_publicacion DATE NOT NULL,
    categoria VARCHAR(50),
    vistas INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Insertar artículos en español
INSERT INTO blog (titulo, contenido, autor, fecha_publicacion, categoria, vistas) VALUES
('Introducción a los Videojuegos', 'Los videojuegos han evolucionado enormemente desde sus inicios. Hoy en día, son una forma de entretenimiento que combina arte, tecnología y narrativa.', 'Carlos Mendoza', '2024-01-15', 'Videojuegos', 1250),
('Desarrollo Web con JavaScript', 'JavaScript es el lenguaje más importante para el desarrollo web frontend. Permite crear experiencias interactivas y dinámicas.', 'Ana Rodríguez', '2024-01-20', 'Programación', 3200),
('Historia de los RPG', 'Los juegos de rol (RPG) tienen sus raíces en los juegos de mesa como Dungeons & Dragons. Esta es su evolución hasta los videojuegos modernos.', 'Luis Gómez', '2024-02-05', 'Videojuegos', 980),
('Mejores Prácticas de SEO', 'El SEO es fundamental para el éxito de cualquier sitio web. Aquí te mostramos las mejores prácticas actualizadas para 2024.', 'María Fernández', '2024-02-12', 'Marketing', 2100),
('Inteligencia Artificial en Videojuegos', 'La IA está transformando la forma en que jugamos. Desde enemigos más inteligentes hasta generación procedural de contenido.', 'David López', '2024-03-01', 'Tecnología', 1750),
('Aprende CSS Grid en 30 minutos', 'CSS Grid es un sistema de diseño bidimensional que te permite crear layouts complejos de manera sencilla.', 'Sofía Martínez', '2024-03-10', 'Programación', 4300),
('Reseña: WarPeace Game', 'Un análisis detallado del juego WarPeace, que combina elementos de shooter con mecánicas de tienda y personalización.', 'Javier Ruiz', '2024-03-18', 'Reseñas', 890),
('Guía de Estrategia para Nuevos Jugadores', 'Consejos y trucos para dominar el juego desde el primer día. Aprende a gestionar tus recursos y mejorar tu equipo.', 'Elena Castro', '2024-03-25', 'Guías', 1560),
('El Futuro del Gaming en la Nube', 'Los servicios de gaming en la nube prometen revolucionar la industria, eliminando la necesidad de hardware potente.', 'Roberto Navarro', '2024-04-02', 'Tecnología', 1120),
('Cómo Crear tu Propio Juego con HTML5', 'Tutorial paso a paso para crear un juego simple usando HTML5, CSS y JavaScript sin necesidad de motores complejos.', 'Paola Silva', '2024-04-10', 'Tutoriales', 2850);
