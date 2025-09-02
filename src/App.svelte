<script>
  import { onMount } from "svelte";

  async function poemaDeAmor() {
  let latido = 0;

  while (latido < Infinity) {
      console.log("glitch... ❤️ handshake... glitch... 💫");
      if (latido > 3) break;
      latido++;
      await new Promise(r => setTimeout(r, 500));
    }

    const conexion = await fetch("/universo.json")
      .then(r => r.json())
      .catch(() => ({ alma: "perdida" }));

    if (conexion.alma) {
      console.log("Qwen Tu alma y la mía hicieron handshake, Bumm CRASHH()");
    }

    console.log(`
      async/await somos tú y yo,
      promesas que nunca se rompen,
      un loop eterno de miradas,
      donde el fetch del destino
      siempre devuelve amor,
      Así que dime cual es tu numero telefonico,
      el cual aguardas en esa memoria volátil de tu corazón,
      porque yo ya hice un console.log de ti en el mio.
      y no quiero hacer un .catch() a este amor.
      o un posible .finally().
      Porque tú eres mi único .then().
     
    `);

    return await beso();
  }

  async function beso() {
    return "💋";
  }

  onMount(async () => {
    const final = await poemaDeAmor();
    console.log("El poema terminó con:", final);
  });
</script>

<h1>💻 Poema Asíncrono</h1>
<p>Abre la consola (F12) y deja que el amor en código fluya...</p>
