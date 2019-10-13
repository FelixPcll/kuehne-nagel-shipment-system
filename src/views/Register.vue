<template>
  <div class="register main-container">
    <div class="presentation">
      <h1>
        Register a New
        <span class="accent">Shipment</span>
      </h1>
      <p>To <span class="accent">Create</span> a new shipment, just fill the form and press the <span class="accent">Register</span> button.</p>
    </div>
    <div class="fields">
      <ul>
        <li v-for="(field, index) in options" :key="field.label">
          <div class="field-container" v-if="field.required">
            <p>{{ field.label }}:</p>
            <input
              :type="field.type"
              :class="`index-${index}`"
              :placeholder="`Insert the ${field.label.toLowerCase()} here...`"
              v-model="model[index]"
              @keyup="formatter(model[index])"
              :maxlength="model[index]!=model.package_weight?field.max_length:null"
            />
          </div>
        </li>
      </ul>
    </div>
    <div class="btn-container">
      <button class="btn-clear" @click="clearBtn()">Clear</button>
      <button class="btn-register" @click="registerBtn()">Register</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data: () => ({
    options: [],
    model: {
      track_ref: '',
      from_coutry: '',
      to_country: '',
      package_weight: 0,
    },
  }),

  methods: {
    getOptions() {
      const apiUrl = 'http://localhost:8000/api/v0.1/shipment/';

      axios
        .options(apiUrl)
        .then((response) => {
          const data = response.data.actions.POST;

          Object.entries(data).forEach(([key, value]) => {
            data[key].type = data[key].type == 'string' ? 'text' : data[key].type;
            data[key].type = data[key].type == 'float' ? 'number' : data[key].type;
          });

          this.options = data;
          // console.log(this.options);
        })
        .catch((e) => {
          console.log(e);
        });
    },

    formatter(field) {
      if (field === this.model.track_ref) {
        this.model.track_ref = field.toUpperCase();
        // alert(`field: ${field}, model: ${this.model.track_ref}`)
      } else if (field === this.model.package_weight) {
        this.model.package_weight = parseFloat(field);
      }
    },

    clearBtn() {
      this.model = {
        track_ref: '',
        from_coutry: '',
        to_country: '',
        package_weight: 0,
      };
    },

    registerBtn() {
      const apiUrl = 'http://127.0.0.1:8000/api/v0.1/shipment/';

      if (this.checkInfo()) {
        axios
          .post(apiUrl, this.model)
          .then((response) => {
            console.log(response);
            alert(`Shipment ${this.model.track_ref} was successfully registered to our database!`);
            this.clearBtn();
          })
          .catch((e) => {
            alert(e);
          });
      }
    },

    checkInfo() {
      if (Object.values(this.model).some(val => val == false)) {
        alert('Plese, insert valid data in all fields');
        return false;
      } if (!confirm('Press "OK" if you confirm that all fields below are correct.')) {
        return false;
      }
      return true;
    },
  },

  created() {
    this.getOptions();
  },
};
</script>

<style lang="scss" scoped>
@import '@/main.scss';

.register {
  margin-top: 40px;

  .presentation {
    h1 {
      font-size: $title-size
    }
  }

  .fields {
    margin-top: 30px;
    // margin-left: 10px;
    ul {
      li {
        margin-bottom: 10px;

        input {
          font-size: $base-size;
          height: 32px;
          //width: 400px;
          padding-left: 5px;
          border: 1.5px solid $baseColor;

          &:focus {
            border-color: $accentColor
          }

          &::placeholder {
            color: rgba($color: $baseColor, $alpha: 0.3)
          }
        }
      }
    }
  }

  .btn-container {
    width: 350px;
    margin-top: 30px;

    button {
      border: 1.5px solid;
      font-size: $base-size;
      padding: 4px 10px 4px 10px;
      background: $bgColor;

      &.btn-clear {
        float: left;
        color: $alertColor;
        border-color: $alertColor;

        &:hover {
          color: $bgColor;
          background-color: $alertColor;
        }

        &:active {
          color: $alertColor;
          border: none;
          background-color: $bgColor;
        }
      }

      &.btn-register {
        float: right;
        color: $baseColor;
        border-color: $baseColor;

        &:hover {
          color: $bgColor;
          background-color: $baseColor;
        }

        &:active {
          color: $baseColor;
          border: none;
          background-color: $bgColor;
        }
      }
    }
  }
}

.field-container {
  .index-track_ref {
    width: 250px;
  }

  .index-to_country {
    width: 350px;
  }

  .index-from_coutry {
    width: 350px;
  }

  .index-package_weight {
    width: 100px;
  }
}

.accent {
  color: $accentColor;
}
</style>
