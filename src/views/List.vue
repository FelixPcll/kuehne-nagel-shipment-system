<template>
  <div class="main-container">
    <div class="display">
      <div class="presentation blk">
        <h1>
          List of Current
          <span class="accent">Shipments</span>
        </h1>
        <p>
          You can
          <span class="accent">Modify</span> or
          <span class="accent">Delete</span> a shipment listed here.
        </p>
      </div>

      <div class="list-itens blk">
        <ListItens />
      </div>
    </div>
  </div>
</template>

<script>
import ListItens from '@/components/ListItens.vue';

export default {
  name: 'list',
  components: {
    ListItens,
  },
};
</script>

<style lang="scss" scoped>
@import "@/main.scss";

.accent {
  color: $accentColor;
}

.display {
  margin-top: 40px;

  .blk {
    display: block;
  }
  .presentation {
    h1 {
      font-size: $title-size;
    }
  }
}
</style>
