provider "helm" {
  kubernetes {
    config_path = "~/.kube/config"
  }
}

provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_namespace" "app" {
  metadata {
    name = "app"
  }
}

resource "helm_release" "api" {
  name      = "api"
  namespace = kubernetes_namespace.app.metadata[0].name

  chart   = "../chart/api"
  version = "0.1.0"

  depends_on = [kubernetes_namespace.app]
}
