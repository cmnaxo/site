function carro(){
    Swal.fire({
      icon: 'success',
      title: 'Producto añadido',
    })
  }
  
  function deleteCart(id_prod){
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
          window.location.href = "/deleteCart/" + id_prod + "/";
        })
      }
    })
  }
  
  function accumCart(id_prod) {
    window.location.href = "/accumCart/" + id_prod + "/";
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
          window.location.href = "/rollCart/";
        });
  }
  
  
  
  