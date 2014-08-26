# generate table html for enight 
from xlsx import Workbook
from jinja2 import Environment, FileSystemLoader

if __name__ == '__main__':
	book = Workbook("E-Night List.xlsx")
	for sheet in book:
		table = []
		for row, cells in sheet.rows().iteritems():
			if row != 1:
				temp = []
				for cell in cells:
					temp.append(cell.value)
				table.append(temp)

		env = Environment(loader=FileSystemLoader('templates'))
		template = env.get_template('table-template.html')
		output_from_parsed_template = template.render(table=table)

		with open("table.html", "wb") as fh:
			fh.write(output_from_parsed_template.encode('ascii', 'xmlcharrefreplace'))
	
