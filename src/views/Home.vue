<template>
  <div class="main-container">
    <div class="display">
      <div class="presentation blk">
        <h1>
          Check the status
          <br />of a
          <span class="emphasize">Shipment</span>.
        </h1>
        <p>
          To create a new instance,
          <span class="emphasize">Register</span> menu.
          <br />To list all the current shipments,
          <span class="emphasize">List</span> menu.
          <br />To retrive a deleted shipment,
          <span class="emphasize">Retrive</span> menu.
        </p>
      </div>
      <div class="card blk">
        <CardInfo />
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import CardInfo from '@/components/CardInfo.vue';

export default {
  name: 'home',
  components: {
    CardInfo,
  },
};
</script>

<style lang="scss" scoped>
@import "@/main.scss";

.emphasize {
  color: $accentColor;
}

.display {
  margin-top: 150px;
  overflow: hidden;
  //background: $washColor;
  .presentation {
    float: left;

    h1 {
      font-size: 5em;
    }
  }
  .card {
    float: left;
    margin-left: 40px;
    margin-top: 40px;
  }
}
</style>
