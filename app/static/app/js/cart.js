const hamburger = document.getElementById('hamburger');
    hamburger.addEventListener('click', function (e) {
        const ul = document.querySelector('nav > ul');
        ul.classList.toggle('menu-slide');
        hamburger.classList.toggle('cross');
});

function anularSuscripcion(){
  const swalWithBootstrapButtons = Swal.mixin({
      customClass: {
        confirmButton: 'btn btn-success',
        cancelButton: 'btn btn-danger'
      },
      buttonsStyling: false
    })
    
    swalWithBootstrapButtons.fire({
      title: '¿Estás seguro de continuar?',
      text: "Podrás volver a suscribirte en un futuro.",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonText: 'Sí',
      cancelButtonText: 'No',
      reverseButtons: true
    }).then((result) => {
      if (result.isConfirmed) {
        window.location.href = "/anularSuscripcion/";
      } else if (
        /* Read more about handling dismissals below */
        result.dismiss === Swal.DismissReason.cancel
      ) {
        swalWithBootstrapButtons.fire(
          'Tu suscripción se mantendrá activa, ¡muchas gracias!',
        )
      }
    })
}

function confirmarSuscripcion(){
  Swal.fire({
      icon: 'warning',
      title: '¿Estás seguro?',
      text: 'Al aceptar la suscripción, se te enviará un correo electrónico con los datos del pago.',
      showCancelButton: true,
      cancelButtonColor: "#d33",
      confirmButtonText: "¡Si, suscribirme!",
      cancelButtonText: "Cancelar"
    }).then((result) => {
      if (result.value) {
        Swal.fire(
          '¡Suscripción realizada!',
          'Te has suscrito',
          'success'
        ).then(function() {
          window.location.href = "/suscribe/";
        })
      }
    })
}

function carro(){
    Swal.fire({
      icon: 'success',
      title: 'Producto añadido',
    })
}
  
function eliminarCarro(id){
    Swal.fire({
      title: '¿Está seguro?',
      text: "El producto será eliminado del carro",
      icon: 'question',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Sí, eliminar!',
      cancelButtonText: 'Cancelar'
    }).then((result) => {
      if (result.isConfirmed) {
        Swal.fire({
            title: "Eliminado!",
            text: "Producto eliminado correctamente",
            icon: 'success'
        }).then (function(){
          window.location.href = "/eliminarCarro/" + id + "/";
        })
      }
    })
}
  
function aumentarCarro(id_prod) {
    window.location.href = "/aumentarCarrito/" + id_prod + "/";
}
  
function PagarCarrito(){
    Swal.fire({
      title: 'Pago realizado',
      text: "Su pago ha sido efectuado correctamente",
      icon: 'success',
      type: 'success',
      confirmButtonColor: '#3085d6',
      confirmButtonText: 'OK',
    }).then(function(){
          window.location.href = "/ResetCarrito/";
        });
}

function alterarEstado(code) {
        Swal.fire({
            title: '¿Está seguro?',
            text: "El estado del pedido será modificado",
            icon: 'question',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Actualizar',
            cancelButtonText: 'Cancelar'
        }).then((result) => {
            if (result.isConfirmed) {
                Swal.fire({
                    title: "Eliminado",
                    text: "Pedido actualizado correctamente",
                    icon: 'success'
                }).then(function () {
                    window.location.href = "/alterarEstado/" + code + "/";
                })
            }
        })
}

  
  
  
  