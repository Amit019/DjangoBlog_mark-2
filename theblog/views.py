from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Category,Comment
from .forms import PostFrom,AddCommentFrom
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.



# !------------ Index View ------------------!

class IndexView(ListView):
    model = Post
    template_name='index.html'   
    ordering=['-publish']

    def get_context_data(self,*args,**kwargs):
        cate_menu =Category.objects.all()
        context =super(IndexView,self).get_context_data(*args,**kwargs)
        context['cate_menu']=cate_menu
        return context

# !------------ end  Index View ------------------!
# !------------ Category View ------------------!

def CategoryView(request,cate):
    category_post= Post.objects.filter(category=cate)
    parmas={'cate':cate.title,'category_post':category_post,}
    return render(request,'category.html',parmas)    


# !------------ end  Category View ------------------!
# !------------  Article Detail  View ------------------!


class ArticleDetailView(DetailView):
    model=Post
    template_name='article_details.html'

    def get_context_data(self,*args,**kwargs):
        cate_menu =Category.objects.all()
        
        context =super(ArticleDetailView,self).get_context_data(*args,**kwargs)
        stuff=get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes=stuff.total_likes()
        liked=False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True
        context['cate_menu']=cate_menu
        context['total_likes']=total_likes
        context['liked']=liked

        return context   

# !------------ end Article  Detail View ------------------!

# !------------ Add Post View ------------------!


class AddPostView(CreateView):
    model=Post
    form_class=PostFrom
    template_name='add_post.html'  
    # fields ='__all__'  
    # fields =('title','body')

# !------------ end Add Post View ------------------!

# !------------ Add Category View ------------------!

class AddCategoryView(CreateView):
    model=Category
    template_name='add_category.html'  
    fields ='__all__'   

# !------------ end Add Category View ------------------!

# !------------ Updateed post View ------------------!


class UpdatedPostView(UpdateView):
    model=Post
    form_class=PostFrom
    template_name='updated.html' 

# !------------ end Updateed post View ------------------!

# !------------ Delete post View ------------------!

class DeletePostView(DeleteView):
    model=Post
    template_name='delete.html' 
    success_url=reverse_lazy('index')

# !------------ end Delete Post View ------------------!   

#  !------------ like View ------------------! 

def LikeView(request,pk):
    post=get_object_or_404(Post,id=request.POST.get('post_id'))
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:    
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('article',args=[str(pk)]))


#  !------------end  like View ------------------! 


#  !------------ Add comment View ------------------! 


class AddCommentView(CreateView):
    model=Comment
    form_class=AddCommentFrom
    template_name='add_comments.html' 
    success_url=reverse_lazy('index') 

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
     
#  !------------end  Add comment View ------------------!   

     
    