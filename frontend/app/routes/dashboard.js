import Ember from 'ember';

export default Ember.Route.extend({
  model: function() {
    /*return Ember.RSVP.hash({
      datasets: this.store.find('dataset'),
      classifiers: this.store.find('classifier')
    })*/
  },

  setupController: function(controller, model) {
     this._super(controller,model);
     controller.set('datasets', this.store.find('dataset'));
     controller.set('classifiers', this.store.find('classifier'));
  }
});
