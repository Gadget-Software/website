<script lang="ts">
  export let title: string;
  export let videoId: string;
  export let autoplay = false;
  export let loop = false;
</script>

<div class="flex flex-col gap-8 mt-10">
  <div class="flex flex-col md:flex-row-reverse items-center md:items-start gap-8 p-8 bg-white rounded shadow">
    <div class="md:w-1/2 flex flex-col gap-4">
      <h3 class="font-bold text-cyan-800 text-lg">
        {title}
      </h3>
      <div class="font-serif">
        <slot />
      </div>
    </div>

    <div class="md:w-1/2">
      <iframe
        class="w-full aspect-video rounded "
        src={`https://www.youtube-nocookie.com/embed/${videoId}?controls=0&autoplay=${autoplay ? 1 : 0}&loop=${loop ? 1 : 0}`}
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
      >
      </iframe>
    </div>
  </div>
</div>
