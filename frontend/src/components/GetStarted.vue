<script setup>
import Button from './Button.vue'
</script>

<template>
    <div class="p-5 flex flex-col justify-between">
        <h2 class="text-2xl">Let's get started!</h2>
        <div class="justify-center">
            <h3 class="text-center text-xl">Click one of the options below to get started:</h3>
            <div class="flex flex-row gap-8 justify-center m-2 mt-5">
                <Button txt="Upload an image" />
                <Button txt="Take a picture" />
            </div>
        </div>
        <div></div>
    </div>
</template>