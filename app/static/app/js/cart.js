function msj(){
  const swalWithBootstrapButtons = Swal.mixin({
      customClass: {
        confirmButton: 'btn btn-success',
        cancelButton: 'btn btn-danger'
      },
      buttonsStyling: false
    })
    
    swalWithBootstrapButtons.fire({
      title: 'Estas seguro de continuar?',
      text: "Podrás volver a suscribirte!",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonText: 'Sí',
      cancelButtonText: 'No',
      reverseButtons: true
    }).then((result) => {
      if (result.isConfirmed) {
        window.location.href = "/CancelarSuscripcion/";
      } else if (
        /* Read more about handling dismissals below */
        result.dismiss === Swal.DismissReason.cancel
      ) {
        swalWithBootstrapButtons.fire(
          'Tu suscripción se mantendrá :)',
        )
      }
    })
}

function carro(){
    Swal.fire({
      icon: 'success',
      title: 'Producto añadido',
    })
  }
  
  function EliminarDeCarrito(id_prod){
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
          window.location.href = "/EliminarDeCarrito/" + id_prod + "/";
        })
      }
    })
  }
  
  function AumentarCarrito(id_prod) {
    window.location.href = "/AumentarCarrito/" + id_prod + "/";
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
  
  
  
  