from GUI import *



class Triangle:
	allTriangles = []

	def __init__(self, p1=None, p2=None, p3=None):
		Triangle.allTriangles.append(self)

		# self.p1 = Vec2(width // 2, 100)
		# self.p2 = Vec2(300, height - 100)
		# self.p3 = Vec2(width - 300, height - 100)

		if p1 == None:
			self.p1 = Vec2.Random(0, width, 0, height)
		else:
			self.p1 = Vec2(p1[0], p1[1])
		
		if p2 == None:
			self.p2 = Vec2.Random(0, width, 0, height)
		else:
			self.p2 = Vec2(p2[0], p2[1])

		if p3 == None:
			self.p3 = Vec2.Random(0, width, 0, height)
		else:
			self.p3 = Vec2(p3[0], p3[1])

	def sign(self, p1, p2, p3):
		return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

	def IsInBounds(self, point):
		d1 = self.sign(point, self.p1, self.p2)
		d2 = self.sign(point, self.p2, self.p3)
		d3 = self.sign(point, self.p3, self.p1)

		has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
		has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

		return not (has_neg and has_pos)

	def Draw(self):
		pg.draw.aaline(screen, white, (self.p1.x, self.p1.y), (self.p2.x, self.p2.y))
		pg.draw.aaline(screen, white, (self.p2.x, self.p2.y), (self.p3.x, self.p3.y))
		pg.draw.aaline(screen, white, (self.p3.x, self.p3.y), (self.p1.x, self.p1.y))


class RandomPoint:
	allRandomPoints = []

	def __init__(self, triangle):
		RandomPoint.allRandomPoints.append(self)

		self.color = white

		self.triangle = triangle

		self.ResetPoint()

	def ResetPoint(self):
		self.point = Vec2.Random(0, width, 0, height)
		while not self.triangle.IsInBounds(self.point):
			self.point = Vec2.Random(0, width, 0, height)

	def GetPoints(self):
		step = 0.5
		random_point = randint(0, 2)
		if random_point == 0:
			x = Lerp(self.triangle.p1.x, self.point.x, step)
			y = Lerp(self.triangle.p1.y, self.point.y, step)
			pg.gfxdraw.pixel(screen, int(x), int(y), self.color)
			self.point = Vec2(x, y)
		
		elif random_point == 1:
			x = Lerp(self.triangle.p2.x, self.point.x, step)
			y = Lerp(self.triangle.p2.y, self.point.y, step)
			pg.gfxdraw.pixel(screen, int(x), int(y), self.color)
			self.point = Vec2(x, y)
		
		elif random_point == 2:
			x = Lerp(self.triangle.p3.x, self.point.x, step)
			y = Lerp(self.triangle.p3.y, self.point.y, step)
			pg.gfxdraw.pixel(screen, int(x), int(y), self.color)
			self.point = Vec2(x, y)


a = height // 2
b = height // 2
x = width // 2
y = height // 2
Triangle(Vec2(x, y), Vec2(x + a, y), Vec2(x, y + b))
Triangle(Vec2(x, y), Vec2(x, y - b), Vec2(x + a, y))
Triangle(Vec2(x, y), Vec2(x - a, y), Vec2(x, y + b))
Triangle(Vec2(x, y), Vec2(x, y - b), Vec2(x - a, y))

for i in range(len(Triangle.allTriangles)):
	p = RandomPoint(Triangle.allTriangles[i])
	p.GetPoints()

screen.fill(black)
fps = 10000000


def DrawLoop():
	# screen.fill(darkGray)

	DrawAllGUIObjects()

	for p in RandomPoint.allRandomPoints:
		p.GetPoints()

	pg.display.update()


def HandleEvents(event):
	HandleGui(event)


def Update():	
	pass	


while running:
	clock.tick_busy_loop(fps)

	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_ESCAPE:
				running = False

		HandleEvents(event)
	
	Update()
	DrawLoop()
