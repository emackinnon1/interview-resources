# from html.parser import HTMLParser


# class Parser(HTMLParser):
#     # method to append the start tag to the list start_tags.
#     def handle_starttag(self, tag, attrs):
#         global start_tags
#         start_tags.append(tag)
#         print("attrs", attrs)
#         # method to append the end tag to the list end_tags.

#     def handle_endtag(self, tag):
#         global end_tags
#         end_tags.append(tag)
#     # method to append the data between the tags to the list all_data.

#     def handle_data(self, data):
#         global all_data
#         all_data.append(data)
#     # method to append the comment to the list comments.

#     def handle_comment(self, data):
#         global comments
#         comments.append(data)


# start_tags = []
# end_tags = []
# all_data = []
# comments = []
# if __name__ == "__main__":
#     # Creating an instance of our class.
#     parser = Parser()
#     # Poviding the input.
#     parser.feed('<html><title>Satyam Blog</title><body><p class="ass face">'
#                 'I love Tea.</p><'
#                 '/body><!--Just started--></html>')
#     print("start tags:", start_tags)
#     print("end tags:", end_tags)
#     print("data:", all_data)
#     print("comments", comments)


