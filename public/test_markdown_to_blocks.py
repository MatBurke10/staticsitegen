import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = ("This is a line \n This is another line")
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, "This is a line \n This is another line")
        return