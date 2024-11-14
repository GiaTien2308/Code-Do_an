import heapq

# Định nghĩa lớp Graph để mô phỏng đồ thị
class Graph:
    def __init__(self):
        self.graph = {}

    # Thêm đỉnh vào đồ thị
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}

    # Thêm cạnh vào đồ thị với trọng số
    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self.graph:
            self.add_vertex(from_vertex)
        if to_vertex not in self.graph:
            self.add_vertex(to_vertex)
        self.graph[from_vertex][to_vertex] = weight
        self.graph[to_vertex][from_vertex] = weight  # Nếu đồ thị vô hướng

    # Thuật toán Dijkstra để tìm đường đi ngắn nhất
    def dijkstra(self, start):
        # Khởi tạo khoảng cách đến tất cả các đỉnh là vô cùng, ngoại trừ đỉnh nguồn
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0

        # Khởi tạo hàng đợi ưu tiên (min-heap)
        priority_queue = [(0, start)]  # (distance, vertex)

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Nếu khoảng cách hiện tại đã lớn hơn khoảng cách đã tính toán, bỏ qua
            if current_distance > distances[current_vertex]:
                continue

            # Duyệt qua các đỉnh kề
            for neighbor, weight in self.graph[current_vertex].items():
                distance = current_distance + weight

                # Nếu tìm thấy đường đi ngắn hơn, cập nhật và thêm vào hàng đợi
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

# Khởi tạo đồ thị và thêm các đỉnh, cạnh
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)

# Tính toán đường đi ngắn nhất từ đỉnh 'A'
start_vertex = 'A'
distances = graph.dijkstra(start_vertex)

# In kết quả
print(f"Khoảng cách từ đỉnh {start_vertex} đến các đỉnh khác:")
for vertex, distance in distances.items():
    print(f"{start_vertex} -> {vertex}: {distance}")
