let estadoSeleccionado = "";

function seleccionarEstado(valor, emoji) {
  estadoSeleccionado = valor;
  document.getElementById("estado-btn").innerText = `${emoji} ${valor}`;
}

async function recomendar() {
  if (!estadoSeleccionado) {
    alert("Selecciona un estado");
    return;
  }

  const response = await fetch(`http://127.0.0.1:5000/recomendar?estado=${estadoSeleccionado}`,);

  const data = await response.json();
  mostrarPeliculas(data);
}

function mostrarPeliculas(lista) {
  const contenedor = document.getElementById("peliculas");

  contenedor.innerHTML = "";

  lista.forEach((pelicula) => {
    contenedor.innerHTML += `
            <div class="card">
                <img src="${pelicula.poster}">
                <div class="card-content">
                    <h3>${pelicula.titulo}</h3>

                    <p>
                        ⭐ ${pelicula.calificacion}
                    </p>
                    <p>
                        ${pelicula.genero}
                    </p>
                    <p>
                        ${pelicula.sinopsis}
                    </p>

                    <button
                        class="favorite-btn"
                        onclick="guardarFavorito('${pelicula.titulo}')">

                        ❤️ Agregar a Favoritos
                    </button>
                </div>
            </div>
        `;
  });
}

async function guardarFavorito(titulo) {

  const usuarioId = localStorage.getItem("usuario_id");

  await fetch("http://127.0.0.1:5000/favoritos",
    {
      method: "POST",

      headers: {
        "Content-Type": "application/json",
      },

      body: JSON.stringify({
        usuario_id: usuarioId,
        titulo: titulo,
      }),
    }
  );

  alert("Película guardada");
}

function mostrarInicio() {
  document.getElementById("inicio").style.display = "block";
  document.getElementById("favoritos").style.display = "none";
}

async function mostrarFavoritos() {
  document.getElementById("inicio").style.display = "none";

  document.getElementById("favoritos").style.display = "block";

  const usuarioId = localStorage.getItem("usuario_id");

  const response = await fetch(`http://127.0.0.1:5000/favoritos/${usuarioId}`);

  const favoritos = await response.json();

  const contenedor = document.getElementById("lista-favoritos");
  contenedor.innerHTML = "";

  favoritos.forEach((f) => {
    contenedor.innerHTML += `
            <div class="card">
                <div class="card-content">
                    <h3>
                        ❤️ ${f.titulo}
                    </h3>
                </div>
            </div>
        `;
  });
}

function mostrarRegistro(){

    document.getElementById("login-form").style.display = "none";

    document.getElementById("register-form").style.display = "block";
}

function mostrarLogin(){

    document.getElementById("register-form").style.display = "none";

    document.getElementById("login-form").style.display = "block";
}

async function cargarInicio(){

    const response = await fetch("http://127.0.0.1:5000/inicio");

    const data = await response.json();

    mostrarPeliculas(data);
}

async function registrar(){

    const nombre = document.getElementById("register-nombre").value;

    const email = document.getElementById("register-email").value;

    const password = document.getElementById("register-password").value;

    const response =
        await fetch("http://127.0.0.1:5000/usuarios",
            {
                method:"POST",

                headers:{
                    "Content-Type":"application/json"
                },

                body:JSON.stringify({
                    nombre,
                    email,
                    password
                })
            }
        );

    if(response.ok){
        alert("Usuario registrado. Ahora inicia sesión.");

        mostrarLogin();

    }
}

async function login(){

    const email = document.getElementById("login-email").value;

    const password = document.getElementById("login-password").value;

    const response =
        await fetch("http://127.0.0.1:5000/login",
            {
                method:"POST",

                headers:{
                    "Content-Type":"application/json"
                },

                body:JSON.stringify({
                    email,
                    password
                })
            }
        );

    if(!response.ok){

        alert("Credenciales inválidas");

        return;
    }

    const usuario = await response.json();

    localStorage.setItem("usuario_id",usuario.id);

    localStorage.setItem("usuario_nombre",usuario.nombre);

    document.getElementById("auth-section").style.display = "none";

    document.getElementById("app-section").style.display = "block";

    cargarInicio();
}

window.onload = () => {

    const usuarioId = localStorage.getItem("usuario_id");

    if(usuarioId){

        document.getElementById("auth-section").style.display = "none";

        document.getElementById("app-section").style.display = "block";

        cargarInicio();

    }else{

        document.getElementById("auth-section").style.display = "flex";

        document.getElementById("app-section").style.display = "none";
    }
};

function logout(){

    localStorage.clear();

    location.reload();
}