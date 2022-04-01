from GUI import *



class Triangle:
	p1 = Vec2(width // 2, 100)
	p2 = Vec2(300, height - 100)
	p3 = Vec2(width - 300, height - 100)

	# p1 = Vec2.Random(0, width, 0, height)
	# p2 = Vec2.Random(0, width, 0, height)
	# p3 = Vec2.Random(0, width, 0, height)

	def sign(p1, p2, p3):
		return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

	def IsInBounds(point):
		d1 = Triangle.sign(point, Triangle.p1, Triangle.p2)
		d2 = Triangle.sign(point, Triangle.p2, Triangle.p3)
		d3 = Triangle.sign(point, Triangle.p3, Triangle.p1)

		has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
		has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

		return not (has_neg and has_pos)


class RandomPoint:
	allRandomPoints = []

	def __init__(self):
		RandomPoint.allRandomPoints.append(self)

		self.color = white

		self.ResetPoint()

	def ResetPoint(self):
		self.point = Vec2.Random(0, width, 0, height)
		while not Triangle.IsInBounds(self.point):
			self.point = Vec2.Random(0, width, 0, height)

	def GetPoints(self):
		random_point = randint(0, 2)
		if random_point == 0:
			x = Lerp(Triangle.p1.x, self.point.x, 0.5)
			y = Lerp(Triangle.p1.y, self.point.y, 0.5)
			pg.gfxdraw.pixel(screen, int(x), int(y), self.color)
			self.point = Vec2(x, y)
		
		elif random_point == 1:
			x = Lerp(Triangle.p2.x, self.point.x, 0.5)
			y = Lerp(Triangle.p2.y, self.point.y, 0.5)
			pg.gfxdraw.pixel(screen, int(x), int(y), self.color)
			self.point = Vec2(x, y)
		
		elif random_point == 2:
			x = Lerp(Triangle.p3.x, self.point.x, 0.5)
			y = Lerp(Triangle.p3.y, self.point.y, 0.5)
			pg.gfxdraw.pixel(screen, int(x), int(y), self.color)
			self.point = Vec2(x, y)

for i in range(1):
	p = RandomPoint()
	p.GetPoints()

screen.fill(black)
fps = 10000000

# pg.draw.aaline(screen, white, (Triangle.p1.x, Triangle.p1.y), (Triangle.p2.x, Triangle.p2.y))
# pg.draw.aaline(screen, white, (Triangle.p2.x, Triangle.p2.y), (Triangle.p3.x, Triangle.p3.y))
# pg.draw.aaline(screen, white, (Triangle.p3.x, Triangle.p3.y), (Triangle.p1.x, Triangle.p1.y))

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
