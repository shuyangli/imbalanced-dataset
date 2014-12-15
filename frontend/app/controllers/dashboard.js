import Ember from 'ember';

export default Ember.Controller.extend({
  datafiles: Ember.computed.mapBy('datasets', 'names'),
  classifier_files: Ember.computed.mapBy('classifiers', 'names'),
  selectedDatasets: [],
  selectedClassifiers: [],
  emptyDatasets: function() {
    var sel_datasets = this.get('selectedDatasets');
    var sel_classifiers = this.get('selectedClassifiers');
    console.log("Empty datasets!");
    console.log(sel_datasets.length);
    console.log(sel_classifiers.length);

    return (sel_datasets.length === 0 || sel_classifiers.length === 0);
  }.property('selectedDatasets', 'selectedClassifiers'),
  actions: {
    submit: function() {
      //alert("Form submitted with the following files!");
      //alert(this.get('selectedDatasets'));
      console.log(this.get('selectedDatasets'));

      var selected_file = this.get('selectedDatasets');
      var selected_classifiers = this.get('selectedClassifiers');
      console.log(selected_classifiers);
      console.log(selected_file);

      var analysis = this.store.createRecord('analysis', {
        'title': "Testing"
      });

      this.store.find('dataset', selected_file).then(function(file) {
        analysis.set('dataset', file);
      });

      /*for(var i = 0; i < selected_classifiers.length; i++) {
        var item = this.store.find('classifier', selected_classifiers[i]);
        analysis.get("classifiers").pushObject(item);
      }*/

      analysis.save();

     /* analysis.save().then(function() {
        console.log("Do something.");
      }, function() {
        console.log("Error!");
      });*/


    }
  }
});
