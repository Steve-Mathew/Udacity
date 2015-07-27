#Udacity
#Nanodegree Program: Introduction to Programming
#Stage: 2
#Project: Automate Web Page
#Due Date: Monday, July 27, 2015
#Student/Author: Steve Mathew
#
#Procedure for Writing this Program:
#
#Present content, composed of Titles and Descriptions of each concept.
#Isolate each concept.
#Isolate each title from each concept.
#Isolate each description from each concept.
#Print HTML for each title and concept.
#Add each HTML segment to the overall HTML code.
#Continue to the next concept, and keep iterating until you run out of concepts.
#Print the entire HTML page.

ContentToPublish = """TITLE: World Wide Web
DESCRIPTION: The World Wide Web is a collection of HTML (HyperText Markup Language) files, most of which are accessible through "hyperlinks".  You can access word-processor files, music, and video files.  In its infancy, the "web", for short, is used to link countless pieces of information together, thus evoking a spider web, which is the source of its namesake.
TITLE: Components
DESCRIPTION: Here are the components that comprise the World Wide Web: The User, Terminal/Computer/Web-Browser, Internet, Communication Protocol (HTTP), Server.
TITLE: HTML
DESCRIPTION: This is composed of content, followed by "markups", which are mostly "tags".  Tags are generally shown by a command enclosed in less-than/greater-than signs, immediately before the content that you wish to mark up, and this is immediately followed by the same tag, except for a slash, signifying the end of markup.
TITLE: Computers and Stupidity
DESCRIPTION: Computers follow instructions explicitly given by the user.  If it's acting "stupid", the "behavior" is likely the user's fault.  So, forgetting to put closing tags, closing quotation marks, and not realizing that hitting "return" on your keyboard is not the same as a line-break tag can result in perceived "stupid" behavior, which is actually the result of human error.
TITLE: Memorization
DESCRIPTION: If you forget how to do something, you can always look it up.  In my opinion, however, it is quite important to know how to do certain things automatically, but that will come with practice.  If you're going to do something that you haven't done in a long time, and can't remember because of this, the Internet is always available.
TITLE: Structure
DESCRIPTION: This contains a heading, which generally consists of a "document type", a heading, a title, then the body, which contains the content that was discussed above.  HTML structures, when shown visually, are analogous to trees.  This is because each element is visualized in a "box", that "branches" out to show other elements contained within, also visualized in "boxes".
TITLE: Boxes and "Boxifying"
DESCRIPTION: This is what developers use to show the complexity of each webpage.  The more "branches" of boxes you have, the more "nested" objects there are.
TITLE: Containers
DESCRIPTION: "Span" and "Div" are containers, which are essentially bigger "boxes" that will have smaller "boxes" nested within.
TITLE: CSS: Definition
DESCRIPTION: CSS stands for "Cascading Style Sheets".  A CSS would normally be its own file, which is referenced by a given HTML, and dictates the appearance of content in that HTML.  The term "cascading" is used, because the concept of "inheritance" is applied.
TITLE: Inheritance
DESCRIPTION: There's an "ancestor/descendant" aspect to "inheritance".  In real life, descendants (offspring, grandchildren, great-grandchildren, etc.) inherit certain traits from their parents, and those traits are carried over to subsequent generations.  In the context of CSS, "ancestor" properties apply to all "descendant" elements.  More importantly, it prevents programmers from having to type the same lines of code over and over again for the same elements.  The time saved can be used for working on other aspects of creating a webpage.  It provides consistency among the same types of elements.
TITLE: Classes
DESCRIPTION: "Classes" are groups of elements, such as a separate section of a webpage, or certain elements within each section of a webpage.
TITLE: Computer
DESCRIPTION: A computer is a device that processes data using binary numbers.  Instructions can be assigned, via programs, allowing a computer to perform calculations, and other more complex tasks.
TITLE: Program
DESCRIPTION: In its simplest form, a program is a set of instructions that tells a computer to perform a specific task.  There are two types of programs: Application Programs and Utility Programs.  Application Programs are basically "hats" that computers wear, allowing them to "play a certain role" in accomplishing a real-world task.  Utility Programs involve perfunctory tasks, that, simply put, involve moving bits and bytes around.
TITLE: Programming Language
DESCRIPTION: This is a "family" of instructions that are designed for a human to communicate with a computer.  Certain programming languages are made for specific industries, such as COBOL (COmmon Business-Oriented Language), for business, and FORTRAN (FORmula TRANslator), for mathematics and science.  Others, such as BASIC (Beginner's All-purpose Symbolic Instruction Code) are for general use.
Python is an example of a programming language.
TITLE: Interpreter
DESCRIPTION: A program that takes instructions, translates them into machine language - one instruction at a time - and executes them immediately.  If an error is found, the program terminates immediately, and an error message showing the line number that caused the abrupt termination will be shown.
TITLE: Compiler
DESCRIPTION: Unlike an Interpreter, a Compiler takes a program, translates all instructions - the source code - into machine language - the object code - and saves this into a file that a computer can execute on its own (such as "executable files").  Programs are run "as-is", with errors undiscovered until after the program executes.  If errors emerge, a program may crash, with the programmer left to his/her own devices to debug the source code.  In the last two decades, Interactive Developer Environments (IDEs) provide tools that will save time in discovering and addressing errors.
TITLE: Grammar
DESCRIPTION: This is essentially a description of what instructions would be considered acceptable and unacceptable in a given programming language.
TITLE: Backus-Naur Form
DESCRIPTION: This is a method of describing the syntax of a given programming language.
TITLE: Nesting
DESCRIPTION: This is essentially putting something within something else, such as creating a List, and creating a new List within the existing List, or creating a FOR Loop, and creating another FOR Loop within the first one.
TITLE: Procedural Thinking
DESCRIPTION: This involves being able to take a task and break it down into simple steps that a computer can follow.
TITLE: Abstract Thinking
DESCRIPTION: This is the ability to find commonality among different kinds of programs.
TITLE: Systems Thinking
DESCRIPTION: This is the ability to take a big problem, and break it down to smaller problems, and to combine the solution to each of those problem to address the big problem.
TITLE: Technological Empathy
DESCRIPTION: This is the ability to "think like a computer", and "understand" what it must be "thinking".
TITLE: Debugging
DESCRIPTION: This is a process by which root causes of program errors are discovered and addressed:  Examine all error messages that you receive.  If your program were derived from an existing program that works, make sure that this existing program works, AND take that existing code, and rework that to fit your requirements.  Assign print statements at various points throughout your code, to check the intermediate values of certain variables.  This may lead to discoveries of errors.  Do your best to keep previous versions of your code, especially if they work properly.  Worst-case scenario: You work from one of those versions.
TITLE: How to Solve Problems
DESCRIPTION: Make sure that you understand the problem.  Understand what the inputs are, and what they represent.  Understand what the given program is supposed to output.  Solve certain test cases manually (by hand).  Start writing code by using simple algorithms, as a foundation for adding more complex code afterward.
TITLE: Variables
DESCRIPTION: A variable is an abstract construct that stores data, whether a number, a character, a string, or a list.
TITLE: Strings
DESCRIPTION: A string is a series of characters, and are not considered to have a numerical value (for all intents and purposes).  A phrase, or an entire sentence, can be considered a string.
TITLE: Indexing Strings
DESCRIPTION: This is a way to search for a character located at a certain position in a string.
TITLE: Subsequence
DESCRIPTION: This is a string, or expression, that is a portion of a larger string or expression.
TITLE: Functions
DESCRIPTION: A function is a subroutine, in that it is a mini-program within a program.  Its purpose is reusable code that programs can call, as if they were regular instructions.
TITLE: IF Statement
DESCRIPTION: This is used to invoke a comparison, and depending on the outcome of this comparison, certain instructions will be executed.
TITLE: WHILE Loops
DESCRIPTION: This is a sequence that reiterates itself as long as certain conditions remain the same.  When those conditions change, this sequence will terminate, and the program will continue.
TITLE: FOR Loops
DESCRIPTION: Unlike a while loop, a FOR loop is used with a specific number of iterations in mind.  In certain programming languages, instead of FOR Loops, they are referred to as DO Loops, since the word "DO" is used instead of "FOR".
TITLE: BREAK Statement
DESCRIPTION: The word "break" automatically terminates a loop that is currently in progress.
TITLE: Lists
DESCRIPTION: Lists are basically a one-dimensional array.
They are more versatile than strings.  Lists are examples of "structured data".
TITLE: Mutability
DESCRIPTION: Mutations are minor changes to lists.  Unlike strings, lists are "mutable".
TITLE: APPEND
DESCRIPTION: Append is a command that adds an item to the end of a list.  This is different from +, which is a concatenation operator.
TITLE: LEN Command
DESCRIPTION: This returns either the length of a string or the number of elements in a list."""

def CreateConceptInHTML(TitleContent, DescriptionContent):
	ConceptInHTML = """
	<div class="Concept">
		<div class="Concept-Title">""" + TitleContent + """</div>
		<p>
			""" + DescriptionContent + """
		</p>
	</div>"""
	return ConceptInHTML

def IsolateConcept(Content, ConceptNumber):
	i = 1
	while i <= ConceptNumber:
		ConceptStartingPoint = Content.find("TITLE:")
		if ConceptStartingPoint == -1:
			Concept = ""
			return Concept
		ConceptEndingPoint = Content.find("TITLE:", ConceptStartingPoint + 6)
		if i == ConceptNumber:
			Concept = Content[ConceptStartingPoint:ConceptEndingPoint]
			return Concept
		else:
			Content = Content[ConceptEndingPoint:]
			i += 1

def IsolateTitle(Concept):
	TitleStartingPoint = Concept.find("TITLE:")
	TitleEndingPoint = Concept.find("DESCRIPTION:")
	TitleContent = Concept[TitleStartingPoint+7:TitleEndingPoint-1]
	return TitleContent
	
def IsolateDescription(Concept):
	DescriptionStartingPoint = Concept.find("DESCRIPTION:")
	DescriptionContent = Concept[DescriptionStartingPoint+13:]
	return DescriptionContent
	
def CreateEntirePage(Content):
	EntirePage = """<!DOCTYPE html>
<html lang="en"> 
<head>
<meta charset="utf-8"/>
	<title>A Primer on the World Wide Web</title>
	<link rel="stylesheet" href="Stage_2_CSS.css">
</head>
<body>
<div class="Section-Title"><u>A Primer on the World Wide Web</u></div>"""
	CurrentConceptNumber = 1
	Concept = IsolateConcept(Content, CurrentConceptNumber)
	while Concept != "":
		TitleContent = IsolateTitle(Concept)
		DescriptionContent = IsolateDescription(Concept)
		EntirePage = EntirePage + CreateConceptInHTML(TitleContent, DescriptionContent)
		CurrentConceptNumber += 1
		Concept = IsolateConcept(Content, CurrentConceptNumber)
	EntirePage = EntirePage + """
	</body>"""
	return EntirePage

print CreateEntirePage(ContentToPublish)
