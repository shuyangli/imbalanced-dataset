import Ember from 'ember';

export default Ember.Controller.extend({

  actions: {
    createDataset: function() {
      //var self = this;
      var dataset = this.store.createRecord('dataset', this.get('fields'));
      var fields = this.get('fields');

      console.log("TESTING");
      console.log(fields);
      console.log(this.get('model'));
      console.log(this.get('name'));
      console.log(this.get('description'));
      console.log(this.get('pos_label'));
      console.log(this.get('dataFile'));
      console.log(this.get('has_header'));
      dataset.save().then(function() {
        self.transitionToRoute('dashboard');
      });
    }
  }
});
