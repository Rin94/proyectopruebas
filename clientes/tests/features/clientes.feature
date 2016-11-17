Feature: Agregar Cliente a sistema:
  Como un administrador de sistema
  quiero registrar un cliente que
  me haya solicitado un servicio y
  almacenarlo en una base de datos
  ya que es complicado mantener
  esa información en formato de hojas de excel.

  Scenario:Agregar a juan primera vez:
  Dado el Formulario de registro se ingresa la siguiente informacion
  |	Primer Nombre	|		|	Confirmar Password	|	Nombre Completo				|	Registrar como				|	Direccion			|	Telefono	|	Codigo Postal	|	Estado		|	Municipio		| Correo electronico	|
  |	juantera5			|	Juancho123	|	Juancho123			|	Juan Francisco Flores Pérez	|	Administrador de Sistema	|	Av. Guerrero 105	|	492106545	|	985645			|	Zacatecas	|	Villa González	|	juancho@uaz.edu.mx	|
  cuando presiono el botón Registrar Adminitrador
  entonces puedo ver el usuario "juantera5" en la lista de administradores registrados
