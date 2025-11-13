<?php

namespace ContainerIw3WgcT;

class CategoriesProviderProxy7ff07d9 extends \PrestaShopBundle\Service\DataProvider\Admin\CategoriesProvider implements \Symfony\Component\VarExporter\LazyObjectInterface
{
    use \Symfony\Component\VarExporter\LazyProxyTrait;

    private const LAZY_OBJECT_PROPERTY_SCOPES = [
        "\0".parent::class."\0".'categories' => [parent::class, 'categories', null, 16],
        "\0".parent::class."\0".'categoriesFromSource' => [parent::class, 'categoriesFromSource', null, 16],
        "\0".parent::class."\0".'categoriesMenu' => [parent::class, 'categoriesMenu', null, 16],
        "\0".parent::class."\0".'modulesTheme' => [parent::class, 'modulesTheme', null, 16],
        'categories' => [parent::class, 'categories', null, 16],
        'categoriesFromSource' => [parent::class, 'categoriesFromSource', null, 16],
        'categoriesMenu' => [parent::class, 'categoriesMenu', null, 16],
        'modulesTheme' => [parent::class, 'modulesTheme', null, 16],
    ];

    public function getCategories(): array
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getCategories(...\func_get_args());
        }

        return parent::getCategories(...\func_get_args());
    }

    public function getCategoriesMenu($modules): array
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getCategoriesMenu(...\func_get_args());
        }

        return parent::getCategoriesMenu(...\func_get_args());
    }

    public function getParentCategory(string $categoryName): string
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getParentCategory(...\func_get_args());
        }

        return parent::getParentCategory(...\func_get_args());
    }
}

// Help opcache.preload discover always-needed symbols
class_exists(\Symfony\Component\VarExporter\Internal\Hydrator::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectRegistry::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectState::class);

if (!\class_exists('CategoriesProviderProxy7ff07d9', false)) {
    \class_alias(__NAMESPACE__.'\\CategoriesProviderProxy7ff07d9', 'CategoriesProviderProxy7ff07d9', false);
}
