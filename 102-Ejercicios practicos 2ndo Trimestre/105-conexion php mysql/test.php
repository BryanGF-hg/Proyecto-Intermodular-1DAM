<?php
 $host = "localhost";
 $user = "blogphp";
 $pass = "Blogphp123$";
 $db   = "blogphp";

 $conexion = new mysqli($host, $user, $pass, $db);

 // Usa el nombre correcto de la columna (ejemplo con 'name')
 $sql = "SELECT * FROM blog";

 $resultado = $conexion->query($sql);

 if ($resultado) {
     while ($fila = $resultado->fetch_assoc()) {
         var_dump($fila);
     }
 } else {
     echo "Error en la consulta: " . $conexion->error;
 }

 $conexion->close();
?>
