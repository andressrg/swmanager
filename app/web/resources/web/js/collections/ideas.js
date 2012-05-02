App.Collections.Ideas = App.Collections.BaseCollection.extend({
	model: App.Models.Idea,
	url: "/api/v1/ideas/",
	parse: function (response){
		this.limit = response.meta.limit;
		this.next = response.meta.next;
		this.offset = response.meta.offset;
		this.previous = response.meta.previous;
		this.total_count = response.meta.total_count;
		
		return response.objects;
	},
	limit: 0,
	next: null, 
	offset: 0, 
	previous: null, 
	total_count: 0	
});
