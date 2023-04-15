<script setup>
    import ImageContainer from './ImageContainer.vue';
    import Button from './Button.vue';
</script>

<template>
    <div class="p-5 flex flex-col justify-between">
        <div>
            <h2 class="text-2xl">Your picture has been banyaynay-ified!</h2>
        </div>
        <div class="justify-center">
                
            <div class="flex justify-center">
                <ImageContainer path="../assets/b1.jpg" />
            </div>
            
        </div>
        <div class="flex justify-between">
                <Button txt="New picture" />
                <Button txt="Save result" />
        </div>   
    </div>
</template>