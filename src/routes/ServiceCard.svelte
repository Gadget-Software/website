<script>
  import Fa from "svelte-fa/src/fa.svelte";

  export let icon;
  export let title = '';
  export let text = '';
</script>

<div class="bg-white flex flex-col justify-between items-center border-2 border-transparent hover:border-cyan-500 rounded-lg shadow-md p-10 gap-4 text-center">
  <div class="text-4xl text-cyan-500">
    <Fa icon={icon} />
  </div>
  <h3 class="font-bold text-2xl">{title}</h3>
  <p>{text}</p>
  <div class="w-[50%] h-[2px] bg-cyan-500"></div>
</div>
