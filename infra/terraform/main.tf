# Definición de Infraestructura como Código

terraform {
  required_providers {
    kubernetes = {
      source = "hashicorp/kubernetes"
      version = ">= 2.0.0"
    }
  }
}

provider "kubernetes" {
  config_path = "~/.kube/config"
}

# 1. Crear un Namespace para Producción
resource "kubernetes_namespace" "production" {
  metadata {
    name = "produccion-real"
  }
}

# 2. Definir límites de recursos (Buenas prácticas)
resource "kubernetes_limit_range" "limits" {
  metadata {
    name      = "limites-recursos"
    namespace = kubernetes_namespace.production.metadata[0].name
  }
  spec {
    limit {
      type = "Container"
      default = {
        cpu    = "200m"
        memory = "512Mi"
      }
    }
  }
}
