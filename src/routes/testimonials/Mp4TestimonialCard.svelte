<script lang="ts">
  import classNames from 'classnames';
  export let title: string;
  export let mp4Src: string;
  export let gifSrc: string;
  export let gifAlt: string;
  export let reverse: boolean = false;
</script>

<div class="flex flex-col gap-8 mt-10">
  <div class={classNames('flex items-center md:items-start gap-8 p-8 bg-white rounded shadow', {
    'flex-col md:flex-row-reverse': !reverse,
    'flex-col md:flex-row': reverse,
  })}>
    <div class="md:w-1/2 flex flex-col gap-4">
      <h3 class="font-bold text-cyan-800 text-lg">
        {title}
      </h3>
      <div class="font-serif">
        <slot />
      </div>
    </div>

    <div class="md:w-1/2">
      <video autoplay loop muted playsinline>
        <source src={mp4Src} type="video/mp4" />
        {#if gifSrc}
        <img src={gifSrc} alt={gifAlt} />
        {/if}
      </video>
    </div>
  </div>
</div>
