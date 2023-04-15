<script setup>
import Button from './Button.vue'
</script>

<template>
    <div class="bg-img flex flex-col items-center p-5 gap-5">
        <h2 class="p-5 text-9xl text-center">Want to find out if ___ is part banana?</h2>
        <Button txt="Get started!" />
    </div>
</template>

<style scoped>
.bg-img {
    background-image: url("../assets/yellow-banana-bg.jpg");
    background-size: cover;
}
</style>