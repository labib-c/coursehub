import time
import uuid

from api.comment.comment import Comment
from db.workers.comment_database_worker import CommentDatabaseWorker


class CommentManager:

    def create_comment(self, course_id, text, user_id, parent_id):
        """

        @type course_id: str
        @type text: str
        @type user_id: int
        @type parent_id: int
        @rtype: comment
        """
        comment_database_worker = CommentDatabaseWorker()
        comment_id = str(uuid.uuid4())
        comment_database_worker.add_children_to_comment(parent_id, comment_id)
        is_root = True
        if parent_id:
            is_root = False
        time_stamp = time.time()
        data = {"id": comment_id, "course_id": course_id, "comment": text,
                "timestamp": time_stamp, "votes": 1, "user_id": user_id, "children": ""}
        comment_database_worker.insert_comment(data)
        return Comment(1, text, time_stamp, course_id, comment_id, user_id, [], is_root)

    def get_comments_by_course(self, course_id):
        """

        @type course_id: str
        @rtype: comment[]
        """
        comment_database_worker = CommentDatabaseWorker()
        return comment_database_worker.get_comments_for_course(course_id)

    def get_comment_by_id(self, comment_id):
        """

        @type comment_id: str
        @rtype: comment
        """
        comment_database_worker = CommentDatabaseWorker()
        result = comment_database_worker.get_comment_by_id(comment_id)
        return Comment(result[4], result[2], result[3], result[1], result[0], result[7], result[6], result[5])

    def upvote(self, comment_id):
        """
        @type comment_id: str
        @rtype: comment

        """
        comment_database_worker = CommentDatabaseWorker()
        comment_to_upvote = self.get_comment_by_id(comment_id)
        comment_to_upvote.set_score(comment_database_worker.upvote(comment_id))
        return comment_to_upvote

    def downvote(self, comment_id):
        """
        @type comment_id: str
        @rtype: comment
        """

        comment_database_worker = CommentDatabaseWorker()
        comment_to_downvote = self.get_comment_by_id(comment_id)
        comment_to_downvote.set_score(comment_database_worker.downvote(comment_id))
        return comment_to_downvote





