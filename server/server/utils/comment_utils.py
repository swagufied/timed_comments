from server.constants import CommentTable

def organize_comments_by_time(comments):

    hashed_comments = {}

    for comment in comments:
        if hashed_comments.get(CommentTable.comment_time):
            # print('here')
            # print(comment)
            hashed_comments[getattr(comment, CommentTable.comment_time)].append({
                CommentTable.ext_username: comment.user.username,
                CommentTable.ext_content: getattr(comment, CommentTable.content)
            })
        else:
            # print(comment)
            hashed_comments[getattr(comment, CommentTable.comment_time)] = [{
                CommentTable.ext_username: comment.user.username,
                CommentTable.ext_content: getattr(comment, CommentTable.content)
            }]
    return hashed_comments
