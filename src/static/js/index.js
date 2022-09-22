
function obtenerDatos(id) {
	document.getElementById("formulario").action = 'update/' + id;
	document.getElementById("boton_formulario").innerHTML = 'Actualizar';
	let name = document.getElementById("table_nombre"+id).innerHTML;
	let apellido = document.getElementById("table_apellido"+id).innerHTML;
	let edad = document.getElementById("table_edad"+id).innerHTML;
	document.getElementById("nombre").value = name;
	document.getElementById("apellido").value = apellido;
	document.getElementById("edad").value = edad;
}