<script setup>
defineProps({
  path: {
    type: String,
    required: true
  }
})
</script>

<template>
    <div class="max-h-[75%]">
        <img :src="path" alt="user uploaded image" />
    </div>
</template>