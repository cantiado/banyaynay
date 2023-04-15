<script setup>
import Button from './Button.vue'
</script>

<template>
    <div class="p-5 flex flex-col bg-mellow-yellow">
        <h2 class="text-2xl">Let's get started!</h2>
        <div class="p-5"></div>
        <h3 class="text-center text-xl">Click one of the options below to get started:</h3>
        <div class="flex flex-row gap-2 justify-center m-2">
            <Button txt="Upload an image" />
            <Button txt="Take a picture" />
        </div>
        <div class="p-5"></div>
    </div>
</template>